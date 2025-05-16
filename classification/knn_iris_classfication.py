'''
Algorithm: K-Nearest-Neighbours
Category: Classification
Data Set: Iris Data Set
'''
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

#feature selection
df = pd.read_csv("iris.csv")
x = df.drop('variety', axis=1)
y = df['variety']

#train test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=40)

#model train
knn = KNeighborsClassifier(n_neighbors=5)
knn = knn.fit(x_train, y_train)

#predict
y_pred = knn.predict(x_test)
accuracy = (accuracy_score(y_test, y_pred)*100)
print(f"Model Accuracy: {accuracy}")

#cm
cm = confusion_matrix(y_test, y_pred, labels=knn.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=knn.classes_)
disp.plot()
plt.title("Iris Classification with KNN")
plt.show()
