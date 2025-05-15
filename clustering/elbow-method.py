'''
Problem: Clustering
Method: Elbow Method (K-MEANS)
Class: Unsuperivzed
Author: Siddhant Nautiyal
'''

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

df = pd.read_csv("iris.csv")
df = df.drop('variety', axis=1)

wcss = []
sil = []
for k in range(1,10):
  kmeans = KMeans(n_clusters=k).fit(df)
  wcss.append(kmeans.inertia_)
  
for k in range(2,10):
  kmeans = KMeans(n_clusters=k).fit(df)
  sil.append(silhouette_score(df,kmeans.labels_))
  
plt.figure(figsize=(12, 5)) 
plt.subplot(1,2,1)
plt.plot(range(1,10), wcss)
plt.xlabel("Value of K")
plt.ylabel("WCSS")
plt.title("Elbow Method")

plt.subplot(1,2,2)
plt.plot(range(2,10), sil)
plt.xlabel("Value of K")
plt.ylabel("Silhouette Score")
plt.title("Clustering Evaluation")
plt.show()
