#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    if True in (1<= t >= 10**9 for t in arr):
        raise TypeError("number must be between 1 and 10^9")
    arr = sorted(arr)
    print(f"{sum(arr[:4])} {sum(arr[-1 : -5 : -1])}")
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)