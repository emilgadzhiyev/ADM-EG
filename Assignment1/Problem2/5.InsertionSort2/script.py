#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#


def insertionSort1(start, arr):
    probe = arr[start]

    for ind in range(start-1, -1, -1):
        if arr[ind] > probe:
            arr[ind+1] = arr[ind]
        else:
            arr[ind+1] = probe
            break
    if arr[0] > probe:
        arr[0] = probe


def insertionSort2(n, arr):
    # Write your code here
    for ind in range(1, len(arr)):
        insertionSort1(ind, arr)
        print(" ".join(map(str, arr)))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
