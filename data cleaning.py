 import pandas as pd #import libarries



df_info=pd.read_csv('analytic_data2021.csv',skiprows=[0]) #load the csv file which contains information of countries and states
df_info=df_info.rename(columns=lambda x: 'x_'+x)  #add prefix x to column names. this data frame will be used to create features

print(df_info.head())

df_info2= pd.read_excel('lagdp1221.xlsx', sheet_name='Sorted')
df_info2=df_info2.rename(columns=lambda x: 'x_'+x)  #add prefix x to column names. this data frame will be used to create features
print(df_info2.head())


df_main=pd.read_csv('COVID-19_Vaccinations_in_the_United_States_County.csv') #load the data set which contains vaccination counts
df_main=df_main.fillna(0) #fill null values with zeros
df_main=df_main.rename(columns=lambda x: 'y_'+x) #add prefix y to column names. data of this data frame will be predicting

print(df_main.head())

#merge two data frames on country and the state
df_final=pd.merge(df_main, df_info, left_on=['y_Recip_County','y_Recip_State'], right_on = ['x_county','x_state'], how='left')
df_final.drop(columns=['y_Recip_County','y_Recip_State'], axis=1, inplace=True) 
'''drop raws which has null values for country and state.
country and state are null means no features to traing a model
'''
df_final=df_final.dropna(subset=['x_county','x_state']) 
df_final['x_county']=df_final['x_county'].apply(lambda x: x.replace(' County', "")) 

#merge two data frames on country and the state
df_final=pd.merge(df_final, df_info2, left_on=['x_county','x_state'], right_on = ['x_County','x_ABB'], how='left')
df_final.drop(columns=['x_County','x_ABB','x_State'], axis=1, inplace=True) 


'''calculate missing value counts and precentages'''
df_missing=pd.DataFrame(df_final.isnull().sum())
df_missing['%']=df_missing[0].apply(lambda x: x*100/len(df_final))

print('columns with zero missing values')
print(df_missing[df_missing[0]==0].index)

'''select columns to drop. if any x column has null values more than 10% those columns will be droped.
 '''
col_drop=[]
col_mis_y=df_missing[df_missing['%']>0].index
col_mis_x=df_missing[df_missing['%']>10].index
for col in col_mis_y:
    if col[0]=='y':
        col_drop.append(col)
    elif col in col_mis_x:
        col_drop.append(col)
df_final.drop(columns=col_drop, axis=1, inplace=True)
df_final=df_final.interpolate() #filling missing values
df_final.to_csv('cleaned_data.csv',index=False)




