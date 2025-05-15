'''
Problem: Clustering
Method: K-Means Clustering
K: 2 (Derived with Elbow Method)
Class: Unsuperivzed
Author: Siddhant Nautiyal
'''

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

df = pd.read_csv("iris.csv")
df = df.drop('variety', axis=1)

kmeans = KMeans(n_clusters=2).fit(df)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

plt.scatter(df.iloc[:, 0], df.iloc[:, 1], c=labels)
plt.scatter(centroids[:, 0], centroids[:, 1], c='blue', marker='X', s=200, label="Centroid")
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Iris Clusters (K=2)')
plt.legend()
plt.show()
