#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    temp = {a: i for i, a in enumerate(arr)}
    swaps = 0
    print(temp)
    for i in range(len(arr)):
        actual, expected = arr[i], i + 1
        actual_i, expected_i = i, temp[expected]
        if actual != expected:
            arr[actual_i] = expected
            arr[expected_i] = actual
            temp[actual] = expected_i
            temp[expected] = actual_i
            swaps += 1
            print("arr is :",arr)
            print("temp is :",temp)
    return swaps

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)
    print(res)
