import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import matplotlib.pyplot as plt


df=pd.read_csv('cleaned_data.csv')


feature_col=['y_Date']
for col in df.columns:
    if col[0]=='x':
        feature_col.append(col)
feature_col.append('y_Completeness_pct')
df_m=df[feature_col]
df_m['y_Date']=df_m['y_Date'].apply(lambda x:int(x.split('/')[2]+x.split('/')[0]+x.split('/')[1]))
df_m=df_m.sort_values(by=['x_county','x_state','y_Date'])
df_m=df_m.reset_index()
df_m.drop(columns=['index','x_county','x_state','y_Date','x_statecode','x_countycode','x_fipscode','x_year'], axis=1, inplace=True)
print(df_m.head())

def series_to_supervised(df,n):   
    #df=df_in.copy()
    for i in range(1,n+1):    
        df2=pd.DataFrame(df['y_Completeness_pct'].shift(i))
        df2.columns=['y_Completeness_pct_'+str(i)]
        m=round(df2['y_Completeness_pct_'+str(i)].mean(),2)
        df2['y_Completeness_pct_'+str(i)].fillna(m,inplace=True)
        df= pd.concat([df, df2], axis = 1)
    df.fillna(0,inplace=True)
    return(df)

df_m_super=series_to_supervised(df_m,4)

print(df_m_super.head())
X=df_m_super.copy()
X.drop(columns=['y_Completeness_pct'], axis=1, inplace=True)

X_scaler = MinMaxScaler()
X_scaled = X_scaler.fit_transform(X)

y_scaler = MinMaxScaler()
y_scaled = y_scaler.fit_transform(np.array(df_m_super['y_Completeness_pct']).reshape(-1,1))
y_scaled=y_scaled.reshape(1,-1)[0]



# pearson's correlation feature selection for numeric input and numeric output
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
fs = SelectKBest(score_func=f_regression, k=65)
# apply feature selection
X_selected = fs.fit_transform(X_scaled, y_scaled)
print(X_selected.shape)

fs.get_feature_names_out(input_features=X.columns)

# split into train and test sets
n_train=int(len(y_scaled)*0.75)
train_X, train_y = X_selected[:n_train, :], y_scaled[:n_train]
test_X, test_y = X_selected[n_train:, :], y_scaled[n_train:]
# reshape input to be 3D [samples, timesteps, features]
train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)

# design network
model = Sequential()
model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2])))
model.add(Dense(1))
model.compile(loss='mae', optimizer='adam')
# fit network
history = model.fit(train_X, train_y, epochs=100, batch_size=10000, validation_data=(test_X, test_y), verbose=2, shuffle=False)

# plot history
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.legend()
plt.show()

yhat = model.predict(test_X)
yhat=y_scaler.inverse_transform(yhat).reshape(-1,1)
y_true=np.array(df_m_super['y_Completeness_pct'])[n_train:].reshape(-1,1)
rmse=np.sqrt(mean_squared_error(y_true, yhat))
print('rmse for testing data:-',rmse)

x=[i for i in range(len(y_true))]
plt.plot(x[:1000],y_true[:1000],c='r',label='true')
plt.plot(x[:1000],yhat[:1000],c='b',label='predicted')
plt.legend()
plt.show()

