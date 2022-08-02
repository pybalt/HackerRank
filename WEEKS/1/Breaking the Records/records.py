#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

scores = [12, 24, 10, 24] #! Ejemplo
result = [24, 10] #! Ejemplo

def breakingRecords(scores:list):
    firstNum = scores[0]
    lowResult = firstNum
    highResult = firstNum

    if not 1<= len(scores) <= 1000:
        raise TypeError("n must be between 1 and 1000")

    lowCounter = 0
    highCounter = 0
    for x in scores:
        if not 0<= x <= 10**8:
            raise TypeError("scores must be between 0 and 10^8")
        
        if x>highResult:
            highResult = x
            highCounter += 1
        if x<lowResult:
            lowResult = x
            lowCounter += 1

    return [highCounter, lowCounter]

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)
    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
