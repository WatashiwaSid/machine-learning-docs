'''
Problem: Dimensioanlity Reduction
Category: Unsupervized
Method: Low Variance Filter
Author: Siddhant Nautiyal
'''

import numpy as np
import pandas as pd
import sys

df = pd.read_csv("reduction.csv")

#variance calculation
#please note this returns a pandas series and not a pandas dataframe
# pd.set_option("display.float_format", "{:.4f}".format)
vs = df.var().round(3)
print(vs)
t = float(input("Enter minimum variance threshold for feature reduction (precision: 3) : "))

#please note this returns a pandas dataframe
rdf = df.loc[:, vs > t]
print(rdf)

#read file name as command line argument to create new file upon dimension reduction
c = int(input("Do you want to save reduced features to a new file? (1: YES, 0: NO) : "))
if(c):
  filename = sys.argv[0]
  with open(f"{filename}_reduced.csv", "x+") as file:
    file.write(rdf.to_string())
  file.close()
  print(f"Reduced features are saved to {filename}_reduced.csv")
