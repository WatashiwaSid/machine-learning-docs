'''
Algorithm: K-Nearest-Neighbours
Category: Classification
Data Set: Iris Data Set
'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


#load dataset to pandas dataframe
df = pd.read_csv('iris.csv')

#feature selection
data_x = df.drop('variety', axis=1) 
data_y = df.variety.values

#Split dataset
x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.25, random_state=42)

#Feature Scaling 
sc = preprocessing.StandardScaler()
x_train_scaled = sc.fit_transform(x_train)
x_test_scaled = sc.transform(x_test)

#Train the model to classify
knn = KNeighborsClassifier()
knn.fit(x_train_scaled, y_train)

#Predict the test set results
y_pred = knn.predict(x_test_scaled)
accuracy = round((accuracy_score(y_test, y_pred)*100),2)
print("Model Accuracy:", accuracy)

#Test for a new dataset
new_iris_data = np.array([[7.3, 2.5, 1.9, 0.33]])
new_iris_scaled = sc.transform(new_iris_data)
new_iris_prediction = knn.predict(new_iris_scaled)
print("New Iris Prediction:", new_iris_prediction)

#Visualization with Seaborn and Matplotlib
plt.figure(figsize=(10, 6))
sns.scatterplot(x=x_test_scaled[:,0], y=x_test_scaled[:, 1], hue=y_test, palette={'Setosa':'blue', 'Versicolor':'green', 'Virginica': 'purple'}, alpha=0.6)
plt.scatter(new_iris_scaled[:, 0], new_iris_scaled[:, 1], color='red', marker='*', s=200, label="New Iris")
plt.title('Iris Variety Classification')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend()
plt.show()
