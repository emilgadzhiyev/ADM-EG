#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#


def viralAdvertising(n):
    # Write your code here
    numOfPeopleAdvertised = 5
    totNumOfPeopleLiked = 0

    for day in range(n):
        numOfPeopleLiked = numOfPeopleAdvertised//2
        totNumOfPeopleLiked += numOfPeopleLiked
        numOfPeopleAdvertised = numOfPeopleLiked*3

    return totNumOfPeopleLiked


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
