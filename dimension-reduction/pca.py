'''
Algorithm: Principal Component Analysis
Dataset: Iris
'''
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

#Feature selection
df = pd.read_csv("iris.csv")
x = df.drop('variety', axis=1)
y = df['variety']

#Standardize the features (essential for pca)
scaler = StandardScaler()
xscaled = scaler.fit_transform(x)

#Apply PCA
pca = PCA(n_components=2)
xpca = pca.fit_transform(xscaled)

#Make Dataframe
dfr = pd.DataFrame(xpca, columns=['PC1', 'PC2'])
dfr['variety'] = y
print(dfr.sample(10))
