#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n:int, k:int, ar:list):
    # Write your code here
    if n not in range(2, 101):
        raise TypeError("n Not in range!")
    if k not in range(1, 101):
        raise TypeError("k Not in range!")
    if type(n) != int or type(k) != int:
        raise TypeError("n & k must been integers!")
    
    count = 0
    print(ar)
    for i in ar:
        if i not in range(1, 101):
            raise TypeError("ar[i] out of range!")
        for j in range(ar.index(i)+1, len(ar)):
            if i < ar[j]:
                count += (i+ar[j])%k == 0
    return count
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    #fptr.write(str(result) + '\n')

    #fptr.close()