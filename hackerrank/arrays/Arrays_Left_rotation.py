#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):

    r = d%len(a)
    arr = [0]*len(a)
    for i in range(len(a)):
        pos = (i + (len(a) - r))%len(a)
        arr[pos] = a[i]

    return arr

nd = input().split()
n = int(nd[0])
d = int(nd[1])
a = list(map(int, input().rstrip().split()))
result = rotLeft(a, d)
print(result)
