'''
Problem: Clustering
Method: Hierarchial Clustering (Agglomerative Method - Bottom Up)
Class: Unsuperivzed
Author: Siddhant Nautiyal
'''

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

df = pd.read_csv("iris.csv")
agglo = AgglomerativeClustering(n_clusters=2).fit(df.iloc[:, 0:2])
labels = agglo.labels_

plt.scatter(df.iloc[:, 0], df.iloc[:, 1], c=labels)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Iris Clusters with Agglomerative Clustering')
plt.show()
