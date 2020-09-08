#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr,n):
    # Write your code here
    s=0
    t=0
    for i in range(n):
        for j in range(n):
            if (i == j):
                s = s + arr[i][j]
           
    for i in range(n):
        for j in range(n):
            if ((i + j) == (n - 1)):
                t = t + arr[i][j]
           
       
    return(abs(s-t))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)

    fptr.write(str(result) + '\n')

    fptr.close()