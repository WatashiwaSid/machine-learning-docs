'''
Algorithm: Logistic Regression Classifier
Dataset: Iris
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

#feature selection
df = pd.read_csv("iris.csv")
x = df.drop('variety', axis=1)
y = df['variety']

#train test split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=30)

#model train
lr = LogisticRegression().fit(x_train, y_train)

#predict
y_pred = lr.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)*100
print(f"Classification Accuracy {accuracy}")

#visualize
cm = confusion_matrix(y_test, y_pred, labels=lr.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=lr.classes_)
disp.plot()
plt.title("Iris Classification with Logistic Regression")
plt.show()
