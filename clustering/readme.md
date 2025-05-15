# Clustering
- Clustering is a technique of unsupervised machine learning where each data point is recognized into a cluster (a group) based on some mutual characteristics. 
- This is different than classification because we are making clusters, not predicting new data points in those clusters.
- Clustering could either be **hard** or **soft**.

## Hard Clustering
- In hard clustering, each data point belongs to one and only one cluster.
- A data point must belong to 1 and only one cluster.
- The are no overlapping clusters.
- Example - **K-Means Clustering** , **K-Medoids Clustering**.

## Soft Clustering
- In soft clustering, a data point could belong to more than 1 cluster at a time.
- Data points share a degree of relationships with clusters based on probability.
- Overlapping clusters are possible.
- Example - **Fuzzy C Means Clustering**, **DBSCAN** (Density-Based Spatial Clustering of Applications with Noise)

## Determining the Optimum Value of K in K-Means
- The right value of K is where the graph stabilizes itself, 2 in this example.
- This can also be confirmed with Silhouette Score, since K=2 has the highest Silhouette Score in this example.
  
![image](https://github.com/user-attachments/assets/55aec1a9-43f3-41b9-a290-abbaf813ba0b)

## Determining the number of clusters in Hierarchial Clustering
- Upon plotting the dendrogram, select the longest vertical line such that no horizontal line passes through it.
- Pass a straight line through this vertical line and count the number of edges.
- The number of edges is the optimum number of clusters.

![Screenshot_2025-05-15_PageMarker](https://github.com/user-attachments/assets/a9440ecb-f97d-46a4-a339-f24ab196d7ff)
