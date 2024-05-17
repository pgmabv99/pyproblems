a=[
    [380,370,360],
    [660,580,560],
    [550,560,500],

    ]

b=[1.80,1.2,0.9]
c=[0,0,0]

prd=0

for j,row in enumerate(a):
    for i,x in enumerate(row) :
        amt=x*b[j]
        print(x, b[j], amt)
        c[j]+=amt

print(c)


# import numpy as np

# # Given matrix
# A = np.array([[3,5,0],
#               [0,-3,-2],
#               [1,3,1]])

# # Calculate the inverse
# A_inv = np.linalg.inv(A)

# print("Inverse of the matrix:")
# print(A_inv)
