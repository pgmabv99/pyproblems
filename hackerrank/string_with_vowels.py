#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def findSubstring(s, k):
    ls=len(s)
    tot=[0]*(ls-k+1)
    for i in range(ls-k+1):
        s1=s[i:i+k]
        # print(i,s1)
        for c in s1:
            print(c)
            if c in ('a','e','i','o','u'):
                tot[i]+=1


    print(tot)
    mv=max(tot)
    if mv :
        imv=tot.index(mv)
        return s[imv:imv+k]
    else:
        return "Not found"

res=findSubstring("azerdii",5)
print(res)

    # Write your code here