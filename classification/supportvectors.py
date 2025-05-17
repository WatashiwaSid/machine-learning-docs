'''
Algorithm: Support Vector Machine (SVM) Classifier
Dataset: Iris
'''
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn import svm
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#feature selection
df = pd.read_csv("iris.csv")
x = df.drop('variety', axis=1)
y = df['variety']

#train test split (4:1)
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.20)

#model train
clf = svm.SVC(kernel='linear').fit(x_train, y_train)

#predict
y_pred = clf.predict(x_test)
accuracy = accuracy_score(y_pred, y_test)*100
print(f"Classification Accuracy: {accuracy}")

#visualize
cm = confusion_matrix(y_test, y_pred, labels=clf.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=clf.classes_)
disp.plot()
plt.title("Iris Classification with Support Vector Machine")
plt.show()
