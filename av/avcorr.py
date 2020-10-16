import numpy as np

import math
from sklearn.linear_model import LinearRegression

x = np.array([0, 5, 15, 25, 35, 45, 55])
# y = np.array([0, 5, 15, 25, 35, 45, 55])
y = np.array([5, 10, 20, 30, 40, 50,60])

print(x)
print(y)

xm=np.mean(x)
ym=np.mean(y)

xmd=x-xm
ymd=y-ym
print("xmd",xmd)
print("ymd",ymd)
t1=xmd*ymd
print("t1",t1)
t2a=xmd*xmd
t2b=ymd*ymd
# t2a=np.power(xmd,2)
# t2b=np.power(ymd,2)
print("t2a",t2a)
corr2=np.sum(t1)/math.sqrt((np.sum(t2a)*np.sum(t2b)))
print("corr", corr2)
print(np.corrcoef(x, y))

