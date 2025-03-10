'''
Algorithm: K-Neighbours Classifier Algorithm
Category: Classification
Data Set: Breast Cancer Prediction Data
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load data
data = pd.read_csv('data.csv')

# Prepare features and labels
data_x = data.drop(['id', 'diagnosis'], axis=1)
data_y = data.diagnosis.values

# Split dataset
train_x, test_x, train_y, test_y = train_test_split(data_x, data_y, test_size=0.25, random_state=42)

# Feature scaling
sc = preprocessing.StandardScaler()
scaled_train_x = sc.fit_transform(train_x)
scaled_test_x = sc.transform(test_x)

# Train KNN model
knn = KNeighborsClassifier()
knn.fit(scaled_train_x, train_y)

# Predict on test data
pred_y = knn.predict(scaled_test_x)
accuracy = round(accuracy_score(test_y, pred_y) * 100, 2)
print(f'Accuracy: {accuracy}%')

# Predict for a new patient record
new_patient_record = np.array([[12.42, 18.38, 77.58, 346.1, 0.1425, 0.2839, 0.2414, 0.1052,
                      0.2597, 0.09744, 0.4956, 2.156, 3.445, 17.23, 0.00911, 0.07458, 0.05661,
                      0.01867, 0.05963, 0.009208, 14.91, 26.5, 97.87, 567.7, 0.2098, 0.8663, 0.6869, 0.2575, 0.6638, 0.173]])

npr_scaled = sc.transform(new_patient_record)
npr_pred = knn.predict(npr_scaled)
print(f'New Patient Prediction: {npr_pred}')

# Scatter plot visualization
plt.figure(figsize=(8, 6))
sns.scatterplot(x=scaled_test_x[:, 0], y=scaled_test_x[:, 1], hue=test_y, palette={"M": "red", "B": "green"}, alpha=0.6)
#plt.scatter(scaled_test_x[:, 0], scaled_test_x[:, 1], c=['red' if y == 'M' else 'blue' for y in test_y], alpha=0.6)
plt.scatter(npr_scaled[:, 0], npr_scaled[:, 1], color='blue', marker='*', s=200, label='New Patient')
plt.xlabel('Feature 1 (Standardized)')
plt.ylabel('Feature 2 (Standardized)')
plt.title('KNN Classification Results')
plt.legend()
plt.show()
