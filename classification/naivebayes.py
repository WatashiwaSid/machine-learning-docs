'''
Algorithm: Naive Bayes Classifier
Category: Classification (Supervised)
Data Set: Iris 
'''
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

#feature selection
df = pd.read_csv("iris.csv")
x = df.drop('variety', axis=1)
y = df['variety']

#train-test split (3:1)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

#model train
nb = GaussianNB()
nb = nb.fit(x_train, y_train)

#Predict the test set results
y_pred = nb.predict(x_test)
accuracy = round((accuracy_score(y_test, y_pred)*100),2)
print("Model Accuracy:", accuracy)

# Confusion matrix
cm = confusion_matrix(y_test, y_pred, labels=nb.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=nb.classes_)
disp.plot()
plt.title("Iris Classification with Naive Bayes")
plt.show()
