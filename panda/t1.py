import pandas as pd
import numpy as np
# df = pd.DataFrame({
#     'A': 1.0,
#     'B': pd.Timestamp('20220101'),
#     'C': pd.Series(1, index=list(range(4)), dtype='float32'),
#     'D': [0,1,2],
#     # 'D': np.array([0,1,2], dtype='int32'),
#     # 'D': np.array([3] * 4, dtype='int32'),
#     'E': pd.Categorical(["test", "train", "test", "train"]),
#     'F': 'foo'
# })
# print(df)
# print(df.describe())


# print(s1)
# print(s1.max())
# print(s1.idxmin())
# m1=s1.mean()
# print("mean",m1)
# print(s1-m1)
# print(s1+100)

# s1=pd.Series([1,2,3,4], index=["a","b","c","d"],name="s1")
# s2=pd.Series([13,12,11],index=["c","b","a"],name="s2")


# # Concatenate Series along axis=1 (columns) to create a DataFrame
# df1 = pd.concat([s1, s2], axis=0, sort=True)
# print("Concatenated DataFrame:\n", df1)
# df2=pd.merge(s1, s2,how="outer", left_index=True, right_index=True )
# print("merged DataFrame:\n",df2)

# df3=pd.DataFrame({"sx1":s1
#                   ,"sx2":s2
#                   })
# print("built dataframe\n",df3)

# Initialize an empty Series
slong = pd.Series([], dtype=int)

# Generate data values and append to the Series
for i in range(5):
    slong = slong._append(pd.Series(i ** 2, index=[f'i_{i}']))

# Name the Series
slong.name = 'slong'
print(slong)