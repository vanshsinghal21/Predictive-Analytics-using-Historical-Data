# Predictive Analytics Using Historical Data

## Overview

This project demonstrates the use of predictive analytics techniques to forecast future trends using historical airline passenger data. A Linear Regression model was trained on historical records to identify patterns and generate future passenger predictions.

## Objective

The objective of this project is to:

* Analyze historical airline passenger data
* Clean and preprocess the dataset
* Build a predictive model using Linear Regression
* Evaluate model performance
* Forecast future passenger trends
* Visualize historical and predicted data

## Dataset

**Dataset:** AirPassengers Dataset

The dataset contains monthly airline passenger counts and is commonly used for time series analysis and forecasting tasks.

### Features

| Feature     | Description                  |
| ----------- | ---------------------------- |
| Month       | Month and Year               |
| #Passengers | Number of Airline Passengers |

## Technologies Used

* Python
* Pandas
* Matplotlib
* Scikit-learn

## Project Workflow

### 1. Data Loading

The AirPassengers dataset was loaded using Pandas.

### 2. Data Preprocessing

* Checked for missing values
* Created a numerical time index for model training

### 3. Model Building

A Linear Regression model was trained using historical passenger data.

### 4. Model Evaluation

Model performance was evaluated using the R² Score.

**R² Score:** 0.8536

### 5. Future Forecasting

The trained model was used to predict passenger counts for the next 12 months.

### 6. Data Visualization

A forecast graph was generated to compare historical trends with predicted values.

## Results

* Successfully trained a predictive model using historical data
* Generated future passenger forecasts
* Achieved an R² Score of 0.8536
* Visualized historical and forecasted trends through a forecasting chart

## Output Files

* `AirPassengers.csv` – Dataset
* `forecast.py` – Python source code
* `forecast.png` – Forecast visualization

## Learning Outcomes

Through this project, I gained practical experience in:

* Predictive Analytics
* Data Preprocessing
* Linear Regression
* Model Evaluation
* Forecasting Techniques
* Data Visualization

## Conclusion

This project demonstrates how historical data can be leveraged to forecast future trends using machine learning techniques. Predictive analytics enables data driven decision making and helps identify future patterns based on past observations.
