# Factors-effecting-vaccine-intake
## **Experimental Design**  
System Information: 
For this study we have used python 3.8 and code has been written on a Jupyter 
notebook. The machine used is based on the Windows 10 platform and available for 
this study has an Intel i5-6442EQ processor, which has 4 cores clocking at 1.90GHz 
and 4GB RAM. Also, for this study MS Excel 2016, SPSS, and Tableau desktop 
2019.1 have been utilized for data manipulation and data visualization. 
####Libraries Used:  
During the duration of this study multiple open source python packages have been 
used. Each one of them have had their own purpose, the packages/libraries that have 
been utilized are as follows: 
● Pandas  
● Numpy  
● Matplotlib.pyplot  
● Seaborn  
● Scikit-learn/Sklearn  
● Tensorflow  
● Keras 
● Pickle 
### Data & Variables 
The datasets that have been used for this project have been mined from open-source 
platforms. The main sources from which data has been obtained are County Health 
Rankings, Centers for Disease Control and Prevention, Bureau of Economic Analysis, 
and National Center for Health Statistics among others. 

##### CHR data: 
The University of Wisconsin Population Health Institute (UWPHI) and the Robert Wood 
Johnson Foundation have been reporting the County Health Ranking (CHR) data 
every year since 2010. Data for the United States counties’ “population health 
checkup” which is in excess of 3000 in number on various health measures is given 
(Remington et. al, 2015). The chief objective of which has been to assist policy and 
decision makers to mobilize action to “raise awareness about the many factors that 
influence health” (Stiefel et. al, 2020). The current ranking system is an extension of 
the annual Wisconsin County Health rankings from 2003 to 2008 to the entirety of the 
United States, which has frequently assisted in facilitating improvement towards 
factors that require more attention (Remington et. al, 2015), engaging communities 
towards improving health, identification of root causes of health issues, keeping track 
of improvement and implementation of health programs (Communities Using 
Rankings Data, 2022).  
The rankings have been roughly divided into two main components, i.e., length of life 
and quality of life. As per [figure], these categories have been further segregated into 
“Health factors”, which is split into health behaviors, clinical care, social and economic 
factors, and physical environment (Remington et. al, 2015).  
For the purposes of our model, the initial variables included were physical health and 
mental factors, alcohol and drug consumption, food quality, uninsured population, 
hospital stays, flu vaccination numbers, education, unemployment, children in poverty, 
crime, air quality, water quality, mortality rate, homeownership, internet access, and 
population variables. The variable selection and data cleaning process will be further 
discussed below.  
#### GDP data 
Gross domestic products GDP data from the Bureau of Economic Analysis (BEA) has 
been taken to represent the economic factor of this study. We have considered the 
GDP data on a regional basis, i.e. the dataset used in the analysis is county level data. 
The Bureau of Economic Analysis releases economic data on a quarterly and annual 
basis which began in 2005 (Landefeld, Seskin and Fraumeni, 2008). The data 
available is vast and the estimates are established through comprehensive census 
data and numerous other statistics which are released every five years. 
There are various measures considered by BEA with are combined to get the final 
number that has been used in the analysis, these are domestic product and income, 
personal income and outlays, government receipts and expenditures (government 
budget data), foreign transactions, saving and investment, income, and employment 
by industry, exports and imports, miscellaneous capital income, etc. 
##### Vaccination Data 
The Centers for Disease Control and Prevention (CDC) crucial data on the COVID
19 pandemic in the United States for monitory purposes including vaccination data. 
We have taken county level data once again for this analysis. CDC collects this 
data using their Vaccine Tracking System (VTrckS), a vaccination order 
management system from judicial, pharmaceutical, and federal organizations. This 
system is able to collect and manage vaccination allocation data, vaccination order 
management information, vaccine shipment data, and is also able to generate 
reports on the complete vaccination distribution procedure. CDC regulates county 
residents through Federal Information Processing Standard State (FIPS) code 
provided to them. This incorporates administered dosage by according to 
jurisdictional clinic partners, retail pharmacies, care facilities, partner dialysis 
centers, Federal Emergency Management Agency (FEMA), and other federal 
organizations (Centers for Disease Control and Prevention, 2022). The data 
selected for the purposes of our model is only a “series_complete” variable by age 
groups- below 5, ages 12 and above, ages 18 and above, and 65 plus. Limitations 
of Data 
##### County health Ranking data 
Since, county health ranking (CHR) data includes any place that has a separate FIPS 
code there have been many additional such “counties”, i.e. counties and county 
equivalents which may be inconsistent between the other two data sources used, for 
example parishes in Louisiana are county equivalents which are not included in GDP 
data (Remington, Catlin and Gennuso, 2015). Also, certain measures in the health 
had high correlations with non-heath related factors, which have not been accounted 
for to keep the underlying socio-economic causes. Furthermore, insufficient data is a 
significant hindrance on CHR data, especially in counties with lower populations. For 
example, excessive drinking have lower values compared to estimated real-world 
numbers, and factors like air quality and obesity are reliant of modelling techniques.   
##### Vaccination Data 
There are certain limitations to this data, as it has been obtained from a secondary 
source county-level data contains these exceptions for the states of California, Hawaii, 
Massachusetts, and New Hampshire. 
● In California, counties with less than 20,000 residents has not been accounted 
for as the state not disclose vaccination uptake in such counties. 
● In New Hampshire after the removal of response declaration on the COVID-19 
emergency, data after May 2021 wasn’t equal to actual number of people opting 
for vaccination. 
● In Massachusetts, incomplete data is available of residents of Barnstable, 
Dukes, and Nantucket. 
● Finally, the state of Hawaii does not declare information of residents in every 
county (Centers for Disease Control and Prevention, 2022). 
Also, vaccination numbers reporting to CDC is the obligation of each state or territorial 
health departments’, hence there is a possibility of difference in reporting times and 
inconsistency may be found between CDC released data and data found on state or 
federal websites.  
##### GDP data 
GDP data has been restricted by the following reason: 
● The previous county of Valdez-Cordova, Alaska (02261) from 2nd January 2019 
has been fragmented into Chugach Census Area (02063) and Copper River 
Census Area (02066). Hence, since 2020 the dollar estimates reflect this 
amendment, however, real chained-dollar values have not been considered. 
● In the state of Virginia independent cities with lower than 100,000 residents is 
pooled together with its neighboring county hence county name are followed by 
the city name. In such scenarios, the combination of such jurisdictions are not 
present (Bureau of Economic Analysis, 2021).   
● Another noteworthy limitation of the GDP data is the many of the components 
considered for the formulation of the final GDP numbers are released every five 
years or real numbers are not available due to different entities being involved 
until after the compilation of GDP numbers by BEA at each quarter like 
consumers federal government expenditures, investment, import and export 
values, therefore, BEA has to utilize “advance” estimates which is done by 
using survey-based monthly information for three months of a quarter, for 
example estimation of inventory is done on the basis of two months of Census 
Bureau data, also import and export estimation is done based on custom 
documents of only two months. Consumer spend on services for each quarter 
are sometimes extrapolations established on monthly trend (Landefeld, Seskin 
and Fraumeni, 2008). 

## Data Preprocessing and Feature Selection 
As explained above the data used for this study is the county health ranking (CHR) 
data, GDP data, and vaccination dataset. For the initial preprocessing of the we have 
selected health factors, education (including proficiency in the English language), 
quality of life which include air quality and water quality, accessibility to the internet, 
homeownership, cost of life, life expectancy, health factors (including sleep patterns, 
hospital visits and its frequency, diabetes and other diseases), social behaviors, 
physical and mental activities, and the state of the living conditions of children in a 
county (including mortality, youth delinquency, juvenile detention rate, etc.).  
However, in the training out the model, all available features have been selected to be 
able to see the variation in feature selection by and empirical and a deep learnt 
method, nevertheless, in the final results a combination of both manual as well as deep 
learn feature selection have been discussed as they were able to provide the most 
significant understanding for this study. A feed forward method has been utilized for 
feature selection. 
Furthermore, the preprocessing of the data cleaning process duty high level of missing 
values due to insufficient data provided by various states and county we have had to 
clean the dataset used. Error detection was done on the data beforehand to yield 
better results on are unsupervised learning approach, also, columns with large amount 
of missing values were dropped. In the preprocessing of training a few limitations of 
the data also came into light, for example county data which were in GDP did not have 
sufficient vaccination or CHR data available and vice-versa, hence had to be dropped 
or imputed.  Furthermore, Columns with missing values and outliers were also 
identified, the missing values were imputed with mean values or state averages for 
certain cases. Moreover, Outlier detection was performed using z-scores and were 
dealt with, binning was also utilized. Also, Different methods have been employed in 
this step as inspired by methods suggested in Winkler, 2003 for unsupervised learning, 
for example we have removed “county”, “city”, “parish”, and “municipality” from the 
county and or state names as we have used data from different sources the name of 
counties differed in each dataset. All three datasets were merged, and examination 
for high correlation between variables in the data, as high correlated variables would 
adversely affect in the modelling process, Pearson’s correlation (Boslaugh and 
Watters, 2008) was used for this access linear relationships between variables. Due to this we were able to see that high correlation was present 
between GDP data from 2018 and 2019, the maximum correlation values was 1.0 and 
the minimum correlation was -0.8385. Moreover, for the purposes of visualizing and 
comparing statistics normalization was also completed for scaling of the data, were 
StandardScaler was deployed for model fit. Lastly, data on vaccination 
was categorized into different age group, for the purposed of this model all age groups 
were aggregated into one variable this was done due to time boundation of this study 
and to manipulate training and fit. We have removed repeating values from the data 
as and selected unique values of counties totaling to 3074 (Appendix 1). 
## Algorithm 
In the modelling process python packages of sklearn and tesnforflow have been 
influential. In study we have adopted the two bidirectional methods based on LSTM 
and GRU networks, i.e. BiLSTM and BiGRU, which are model1 and model2, 
respectively. For the purpose of the model, each county value is transformed into 
sequential chunks. Model is split into training and testing sets through random seed, 
and creation of a data structure is done with seven timesteps and a single output.  
Training of the model has been processed primarily through the tensorflow version 
2.4.4.
#### Model1: 
The LSTM layer is comprises on a sequences of LSTM cells, and data is 
initially in a forward direction, however, another backward feed layer is also taken as 
discussion the section (RM) for a bidirectional LSTM layer, with a linear activation. 
Loss taken into consideration for the model is mean square error (MSE) as the loss 
function for evaluation, and Adam optimizer, an algorithm that is used to update 
weights of the network. The batch size taken for this is 64 and is trained for 5 epochs, 
with a 0.2 validation split and 1 equivalent to verbose. The model is evaluated mean 
squared error (MSE). 
#### Model2:
In this model we have adopted GRU mechanism of RNN. Similarly to model1, 
the layers here is also bidirectional, i.e. a BiGRU. There is a singular output and a 
linear activation, with loss assessed through mean square error, and an Adam 
optimizer. The batch size taken here is 64, as GRU is able to achieve fast processing 
speeds. This model has also been trained at 5 epochs, again with a validation split of 
0.2 and verbose equal to 1.  
Finally, the both BiLSTM and BiGRU models have been investigated through Local 
Interpretable Model-agnostic (LIME) tool for comprehending the effects of individual 
features of the models used.  
