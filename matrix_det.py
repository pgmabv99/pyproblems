# import numpy as np

# # Define your matrix
# m = np.array([[3,4,5], [-4,5,1],[-1,-3,4]])
# mx = np.array([[2,4,5], [3,5,1],[1,-3,4]])


# # Calculate the determinant
# dm = np.linalg.det(m)
# dmx = np.linalg.det(mx)
# x=dmx/dm
# print(dm,x)

import numpy as np
import matplotlib.pyplot as plt

# Define the range of theta values
theta = np.linspace(0, 2*np.pi, 1000)

# Calculate r for each theta
r = 3 * np.sin(2 * theta)

# Convert polar coordinates to Cartesian coordinates
x = r * np.cos(theta)
y = r * np.sin(theta)

# Plot the graph
plt.figure(figsize=(8, 8))
plt.plot(x, y, color='blue')
plt.title('Graph of r = 3sin(2θ)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axis('equal')
plt.show()

