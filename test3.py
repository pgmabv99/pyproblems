import pandas as pd
import csv
from IPython.display import display, HTML

# Write your code herep

df= pd.read_csv("./root/customers/data.csv") 
# Preview the first 5 lines of the loaded data 
# data.head()
display(df)






# ---------
print("Total customers:")
print(df['ID'].count())

# -------------?
print("Customers by city:")
df1=df.groupby(['CITY']).count()
df2=df1.sort_values(['CITY'])
for row in df2.itertuples():
    print(row.Index+":",row.ID)

print("Customers by country:")
df1=df.groupby(['COUNTRY']).count()
df2=df1.sort_values(['COUNTRY'])
for row in df2.itertuples():
    print(row.Index+":",row.ID)

print("Country with the largest number of customers' contracts:")

df1=df.groupby(['COUNTRY']).sum()
dfmax=df1['CONTRCNT'].max()
dfflt = df1[df1['CONTRCNT'] == dfmax].sort_values('COUNTRY')
for row in dfflt.itertuples():
    print(row.Index+":",dfmax)


print("Unique cities with at least one customer:")