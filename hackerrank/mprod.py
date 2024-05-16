a=[
    [380,370,360],
    [660,580,560],
    [550,560,500],

    ]

b=[0.40,0.80,1.30]

# prd=0

# for j,row in enumerate(a):
#     for x in row:
#         amt=x*b[j]
#         if j >0 :
#             continue
#         prd+=amt
#         print(x, b[j], amt)
#         print(prd)

# print(prd)


import numpy as np

# Given matrix
A = np.array([[3,5,0],
              [0,-3,-2],
              [1,3,1]])

# Calculate the inverse
A_inv = np.linalg.inv(A)

print("Inverse of the matrix:")
print(A_inv)
