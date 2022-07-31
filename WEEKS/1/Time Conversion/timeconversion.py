#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    from datetime import datetime as dt
    dateObject= dt.strptime(s.upper(), '%I:%M:%S%p').time() #Because the date is given in %I format
    
    return (dateObject.strftime('%H:%M:%S'))
    
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #s = input()

    result = timeConversion('07:05:45AM')

    #fptr.write(result + '\n')

    #fptr.close()
