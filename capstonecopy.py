#imports
import dash
import pandas as pd
import numpy as np
from dash import Dash, html, dcc, Input, Output, callback
import streamlit as st
import folium
import plotly.express as px
import pandas as pd
import numpy as np
import requests as rq
import bs4
import pandas as pd
import plotly.express as px
import numpy as np
import streamlit as st
from io import StringIO
import datetime
from sklearn.linear_model import LinearRegression

#read CSV files
df1 = pd.read_csv("2000-2009.csv")
df2 = pd.read_csv("2010-2019.csv")
df3 = pd.read_csv("2020-Present.csv")
df = pd.concat([df1, df2, df3], ignore_index=True)  #combine all files in 1 df

df = df[['Date', 'Maximum Temperature degrees (F)', 'Minimum Temperature degrees (F)', 'Precipitation (inches)', 'Snow Depth (inches)']]    #keep these columns

df['Precipitation (inches)'] = df['Precipitation (inches)'].astype(str) #treat this column as a string to prepare for the search in the next step
df['Snow Depth (inches)'] = df['Snow Depth (inches)'].astype(str)

df.loc[df['Precipitation (inches)'].str.contains('T'), 'Precipitation (inches)'] = ((float('0.00')))    #replace trace data as 0.00
df.loc[df['Snow Depth (inches)'].str.contains('T'), 'Snow Depth (inches)'] = ((float('0.00')))

df['Precipitation (inches)'] = df['Precipitation (inches)'].astype(float)   #convert this data to float for future calculations
df['Snow Depth (inches)'] = df['Snow Depth (inches)'].astype(float)

df['Date'] = pd.to_datetime(df['Date']) #convert date
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df = df[['Date', 'Year', 'Month', 'Day', 'Maximum Temperature degrees (F)', 'Minimum Temperature degrees (F)', 'Precipitation (inches)', 'Snow Depth (inches)']]    #break down 
#date to year/month/day

#1. average
df2 = df.groupby(['Month', 'Day'])['Snow Depth (inches)'].mean().reset_index()  #calculate average snow depth based on day/month
df2 = df2.rename(columns={'Snow Depth (inches)': 'Average Snow Depth'}) 

df = df.merge(df2, on=['Month', 'Day'], how='left') #add average snow depth calculation data in original df for future data pulling


#2. linear regression
train = df[df['Year'] < 2024]   #training data is based on all data for years before 2024
test2024 = df[df['Year'] == 2024].copy()    #testing data is based on 2024

parameters = ['Year', 'Month', 'Day', 'Maximum Temperature degrees (F)', 'Minimum Temperature degrees (F)', 'Precipitation (inches)']   #parameters which are relevant for
#predicting average snow depth
X_train = train[parameters] #creates parameters for training
y_train = train['Snow Depth (inches)']  #snow depth data to be used for training (data for years prior to 2024)
X_test = test2024[parameters]   #2024 parameter data is what will be tested for predictions

model = LinearRegression()
model.fit(X_train, y_train) #fit the linear regression, using training data 
pred2024 = model.predict(X_test)    #create prediction data using 2024 parameter data

test2024['Predicted 2024 data'] = pred2024  


st.markdown(
    """
<style>
.reportview-container .main{
background-color: #ADD8e6;
}
</style>
""",
unsafe_allow_html=True,
)

st.set_page_config(
    page_title="2024 Snow Depth Predictor versus Actual versus Average"
)


selectdate = st.date_input("select date in 2024", min_value=datetime.date(2024, 1, 1), max_value=datetime.date(2024, 12, 31))    #allow user to enter date

month = selectdate.month    #stores the user selected month and day within 2024 as month and day
day = selectdate.day

row = test2024[(test2024['Month'] == month) & (test2024['Day'] == day)] #create a df called "row" from the test2024 df that will match the month and day

snowplot = px.bar(df, x ="Date", y ="Average Snow Depth")   #create a plot for visualization

if row.empty:
    st.write("no data")

else:
    st.write("predicted snow depth (in): ", row['Predicted 2024 data'].values[0])
    st.write("average snow depth (in): ", row['Average Snow Depth'].values[0])      
    st.write("actual snow depth (in): ", row['Snow Depth (inches)'].values[0])

st.plotly_chart(snowplot)