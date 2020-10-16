import numpy as np
import pandas as pd
import math
from sklearn.linear_model import LinearRegression



# ages = pd.Series([5, 10, 15], name="Age")
# print(ages)
# ages2 = -ages + 5
# print(ages2)
# print(ages.corr(ages2))


df = pd.DataFrame({
    "Name": ["Braund, Mr. Owen Harris",
             "Allen, Mr. William Henry",
             "Bonnell, Miss. Elizabeth"],
    "Age": [22, 35, 58],
    "Sal" : [10, 30, 50],
    "Sex": ["male", "male", "female"]}
)

# print(df["Age"])
# print("max",df["Age"].max())
# print(df["Age"].describe())
s1=df["Age"]
print("s1 \n",s1)
print("corr",df["Age"].corr(df["Sal"]) )