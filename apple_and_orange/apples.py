#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    c=0
    c1=0
    for i in range(len(apples)):
        j=a+apples[i]
        if(j in range (s,t+1)):
            c=c+1
    for i in range(len(oranges)):
        j=b+oranges[i]
        if(j in range (s,t+1)):
            c1=c1+1
            
    print(c)
    print(c1)
    


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

