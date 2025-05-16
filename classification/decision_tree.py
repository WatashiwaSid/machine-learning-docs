'''
Algorithm: Decision Tree Classifier
'''
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#feature selection
df = pd.read_csv('iris.csv')
x = df.drop('variety', axis=1) 
y = df['variety']

#Split dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

#Model training
dt = DecisionTreeClassifier()
dt.fit(x_train, y_train)

#Predict the test set results
y_pred = dt.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)*100
print("Model Accuracy:", accuracy)

# Visualizing the Decision Tree
plt.figure(figsize=(12, 8))
plot_tree(dt, feature_names=x.columns, class_names=dt.classes_)
plt.title("Decision Tree Visualization")
plt.show()
