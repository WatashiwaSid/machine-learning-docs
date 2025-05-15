'''
Problem: Clustering
Method: Dendrogram (Hierarchial Clustering)
Class: Unsuperivzed
Author: Siddhant Nautiyal
'''

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import scipy.cluster.hierarchy as sc

df = pd.read_csv("iris.csv")

plt.figure(figsize=(20,8))

#df.iloc[:, 0:2] = First Two Columns 
sc.dendrogram(sc.linkage(df.iloc[:,0:2], method='ward')) 
plt.xlabel('Data')
plt.ylabel('Eucledian Distance')
plt.title('Iris Dendrogram')
plt.show()
