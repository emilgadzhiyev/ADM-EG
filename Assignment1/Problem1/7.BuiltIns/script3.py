# Athlete Sort

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
import os
import random
import re
import sys

N, M = map(int, input().split())
rows = [input() for _ in range(N)]
K = int(input())

for row in sorted(rows, key=lambda row: int(row.split()[K])):
    print(row)
