import numpy as np
import matplotlib.pyplot as plt
import time

from numpy.core.shape_base import block

def mydraw(test):
    plt.clf()
    plt.imshow(test)
    # plt.colorbar()
    plt.show(block=False)
    plt.pause(1)
    

n =11
test= np.full((n,n),0)
for i in range(n):
    test[i,i]=9
    mydraw(test)
    
time.sleep(4)
