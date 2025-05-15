'''
Problem: Clustering
Method: DBSCAN Algorithm
Class: Unsuperivzed
Author: Siddhant Nautiyal
'''
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons
from sklearn import preprocessing

#generate non-linear synthetic data for dbscan clusters
x,y =  make_moons(n_samples=250, noise=0.05)

#value of noise and epsilon were derived with hit and trial
db = DBSCAN(eps=0.15).fit(x)
labels = db.labels_

plt.scatter(x[:, 0], x[:, 1], c=labels)
plt.xlabel('Feature X')
plt.ylabel('Feature Y')
plt.title('DBSCAN Clustering Algorithm')
plt.show()
