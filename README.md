Anura Khond
EN.585.771.81.FA25
Capstone Project - 2024 Snow Depth Predictor versus Actual versus Average
MD README file

The purpose of this project is to pull weather data (date, temperature, precipitation, snow depth) in Minneapolis/St.Paul, Minnesota from 2000-2023 and to allow the user to select a date in 2024 to find the predicted snow depth for that specific day.

The source for data is found here: https://www.dnr.state.mn.us/climate/twin_cities/listings.html. This site contains the Excel and CSV files for each decade.

There were 2 approaches for this:
1. Calculate the average snow depth for that specific day across all the years
2. Predict the snow depth for that specific day, using testing/training data sets and linear regression, to factor in temperature and precipitation across all the years

The data web app shows the side-by-side comparison for the following 3 for the specific day selected by the user:
1. Average snow depth, based on 2000-2023 data (snow depth parameter only)
2. Predicted snow depth, based on 2000-2023 data (temperature, precipitation, snow depth parameters)
3. Actual snow depth, based on 2024 data
This allows the user to compare what the average snow depth is and what the linear regression prediction is. 

By comparing the 3 values, the user can see how temperature/precipitation can impact the actual snow depth (for example, due to global warming or climate patterns) and how the basic average may not be an accurate predictor.

A plot is also generated for extra data visualization.

link to video:https://livejohnshopkins-my.sharepoint.com/:v:/r/personal/akhond1_jh_edu/Documents/Biomedical%20Data%20Science%20-%20Fall%202025/Anura%20Khond%20Capstone%20Project%20Biomedical%20Data%20Science.mp4?csf=1&web=1&e=V2rBIK&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbE1vZGUiOiJtaXMiLCJyZWZlcnJhbFZpZXciOiJwb3N0cm9sbC1jb3B5bGluayIsInJlZmVycmFsUGxheWJhY2tTZXNzaW9uSWQiOiIwNWE1ZDNhZC1lMmU2LTQxNWQtYWI4Zi1mNDg1NGZjODlkMWIifX0%3D