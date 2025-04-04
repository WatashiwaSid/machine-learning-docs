'''
Problem: Clustering
Method: K-Means Clustering
Class: Unsuperivzed
Author: Siddhant Nautiyal
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load data
df = pd.read_csv("cluster.csv")

# Fit KMeans model
kmeans = KMeans(n_clusters=2, random_state=0, n_init=10).fit(df)

# Get cluster labels and centroids
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Predict a new data point
new_point = np.array([[175, 65]])
predicted_cluster = kmeans.predict(new_point)
print(f"Predicted cluster for {new_point.tolist()[0]}: {predicted_cluster[0]}")

# Visualization
plt.figure(figsize=(7, 7))
plt.scatter(df.iloc[:, 0], df.iloc[:, 1], c=labels, cmap='viridis', alpha=0.7, edgecolors='k')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.scatter(new_point[:, 0], new_point[:, 1], c='blue', marker='P', s=150, label='New Point')
plt.xlabel("Feature X")
plt.ylabel("Feature Y")
plt.legend()
plt.title("K-Means Clustering")
plt.show()
