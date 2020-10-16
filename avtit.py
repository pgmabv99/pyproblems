import numpy as np
import pandas as pd
import math
from sklearn.linear_model import LinearRegression



t = pd.read_csv("files/titanic.csv")
# print(t.dtypes)
# print(t[["Age","Sex"]].head(3))
# print(t[t["Age"]>30] & t["Pclass"].isin([1,2]))
print(t.loc[(t["Age"]>30) & (t["Pclass"].isin([1,2])),"Age"])