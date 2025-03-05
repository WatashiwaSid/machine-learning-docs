'''
Problem: Feature Scaling For Classification Problem
Introduction:
Feature Scaling is important to fit features in an optimized range, otherwise some features could have more standing in the model than other features, resulting in a biased beahviour.
Feature scaling could be done using Normalization or Standardization.

Author: Siddhant Nautiyal
Dataset - Iris Dataset (kaggle)
Link to dataset: https://www.kaggle.com/datasets/saurabh00007/iriscsv/data
Terminology:
Feature: Independent Variables (x)
Predictor: Dependent Variable (y)
'''

import pandas as pd

# #loading the dataset and viewing first 5 records
from sklearn import preprocessing
data_set = pd.read_csv("iris.csv")
# data_set.head(5)

#feature selection
x = data_set.iloc[:5, 0:4].values 
print("Original Values: \n", x)


# feature scaling (min-max normalization)
minMaxNormalized = preprocessing.MinMaxScaler(feature_range =(0, 1)) #scale values to fit in range 0-1
scaled_x = minMaxNormalized.fit_transform(x);

print("Values after min-max normalization: \n", scaled_x)
