#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    #* Constraints:
        #* 1.  : 0 < n <= 100
        #* 2.  : -100 <= arr[i] <= 100
    
    if not 0 < n <= 100:
        raise TypeError("n must be between 0 and 100")
    positives = 0
    negatives = 0
    zeros = 0
    for i in arr:
        if not -100 <= i <= 100:
            raise TypeError("integers must be between -100 and 100")
        if i > 0:
            positives += 1
        if i < 0:
            negatives += 1
        if i ==0:
            zeros += 1
    print(f"""{format(positives/n, ".6f")}
{format(negatives/n, ".6f")}
{format(zeros/n, ".6f")}""")

if __name__ == '__main__':
    
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
