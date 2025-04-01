from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
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

#Model training
dt = DecisionTreeClassifier()
dt.fit(x_train_scaled, y_train)

#Predict the test set results
y_pred = dt.predict(x_test_scaled)
accuracy = round((accuracy_score(y_test, y_pred)*100),2)
print("Model Accuracy:", accuracy)

# Visualizing the Decision Tree
plt.figure(figsize=(12, 8))
plot_tree(dt, feature_names=data_x.columns, class_names=df['variety'].unique(), filled=True)
plt.title("Decision Tree Visualization")
plt.show()
