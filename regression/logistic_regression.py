'''
Author - Siddhant Nautiyal
Problem - Logistic Regression
Class - Regression
Category - Supervised Learning
'''

import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv')

#remove Setosa variety from the dataframe for binary classification
df = df[df['variety'] != 'Setosa']

#Encode class labels to 0 and 1
df['variety'] = df['variety'].map({'Versicolor':0, 'Virginica':1})

#split predictors and outcome
x = df.iloc[:,:-1]
y = df.iloc[:,-1]

#train test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=40)
rg = LogisticRegression()

#train
rg.fit(x_train, y_train)

#prediction
y_pred = rg.predict(x_test)

#performance metrics
acc = accuracy_score(y_pred, y_test)
cm = confusion_matrix(y_test, y_pred)
print(f"Accuracy: {round(acc*100,2)}")

#visualize
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Versicolor', 'Virginica'], yticklabels=['Versicolor', 'Virginica'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
