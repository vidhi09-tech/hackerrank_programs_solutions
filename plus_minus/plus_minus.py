#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p=0
    q=0
    r=0
    for i in range(len(arr)):
        if(arr[i]>0):
            p+=1
        elif(arr[i]<0):
            q+=1
        else:
            r+=1
    print(p/len(arr))
    print(q/len(arr))
    print(r/len(arr))
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
