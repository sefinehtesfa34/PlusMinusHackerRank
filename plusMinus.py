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
    for i in arr:
        pos=0
        neg=0
        zer=0
        for i in arr:
            if i>0:
                pos+=1
            if i==0:
                zer+=1
            if i<0:
                neg+=1
    posRatio=(pos/len(arr))
    negRatio=(neg/len(arr))
    zerRatio=(zer/len(arr))
    print("%.6f" %(posRatio))
    print("%.6f" %(negRatio))
    print("%.6f" %(zerRatio))
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
