#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
def arrayManipulation(n, queries):
    # Write your code here
    mi, mj, mv=-1, -1, 0
    for q in queries:
        i, j, v=q
        i=max(1, i)
        j=min(n, j)
        if i> mj or mi > j:
            # no inter
            if v > mv:
                mv, mi, mj= v,i,j
            print(" no inter", mi, mj, mv)
        else:
            # compute inter
            mi=max(mi, i)
            mj=min(mj, j)
            mv+=v
            print(" yes inter", mi, mj, mv)
    return mv

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
