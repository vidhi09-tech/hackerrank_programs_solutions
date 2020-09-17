<<<<<<< HEAD
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    mincount=maxcount=0
    minscore=maxscore=scores[0]
    for i in range (1, len(scores)):
        if minscore<scores[i]:
            minscore=scores[i]
            mincount+=1
        elif maxscore>scores[i]:
            maxscore=scores[i]
            maxcount+=1
    return mincount, maxcount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

=======
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    mincount=maxcount=0
    minscore=maxscore=scores[0]
    for i in range (1, len(scores)):
        if minscore<scores[i]:
            minscore=scores[i]
            mincount+=1
        elif maxscore>scores[i]:
            maxscore=scores[i]
            maxcount+=1
    return mincount, maxcount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

>>>>>>> 44a13ad01901b9c33d8d28551b5aa0c40e384243
    fptr.close()