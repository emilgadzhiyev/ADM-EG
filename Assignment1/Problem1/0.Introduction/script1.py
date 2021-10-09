# Python If-Else

#!/bin/python3
import math
import os
import random
import re
import sys

# Initial solution
# if __name__ == '__main__':
#     n = int(input().strip())
#     # If n is odd,
#     # print Weird
#     if (n % 2) != 0:
#         print('Weird');
#     # If n is even and in the inclusive range of 2 to 5,
#     # print Not Weird
#     if (n % 2 == 0) and ((n >= 2) and (n <= 5)):
#         print('Not Weird')
#     # If n is even and in the inclusive range of 6 to 20,
#     # print Weird
#     if (n % 2 == 0) and ((n >= 6) and (n <= 20)):
#         print('Weird')
#     # If n is even and greater than 20,
#     # print Not Weird
#     if (n % 2 == 0) and n > 20:
#         print('Not Weird')

# Or little bit another solution
# I prefered to commit first one, because it's obviously.
# And the HackerRank's bot can't analyze live code (unit test accept only 1 result)
n = int(input().strip())
startRange = 2
endRange = 5
startRange2 = 6
endRange2 = 20
number = 20
if n % 2 != 0:
    print("Weird")
else:
    if (n >= startRange) and (n <= endRange):
        print("Not Weird")
    if (n >= startRange2) and (n <= endRange2):
        print("Weird")
    if n > number:
        print("Not Weird")
