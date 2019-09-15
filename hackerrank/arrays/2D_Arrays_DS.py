import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_sum = -900000000000
    sum = 0
    for i in range(0,6):
        for j in range(0,6):
            if i < 4 and j < 4:
                sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
                if max_sum < sum:
                    max_sum = sum
                    sum = 0
    return max_sum


arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

result = hourglassSum(arr)
print(result)
