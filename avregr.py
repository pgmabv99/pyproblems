import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([0, 5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 10, 20, 30, 40, 50,60])
# x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))

# y = np.array([5, 20, 14, 32, 22, 38])
print(x)
print(y)
m=LinearRegression().fit(x,y)
print("intercept", m.intercept_, "coef",   m.coef_)
print("score",m.score(x,y))

x_new = np.arange(5).reshape((-1, 1))
print("Y_new", x_new, m.predict(x_new))