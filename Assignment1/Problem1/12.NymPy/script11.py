# Dot and Cross

# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

n = int(input())
a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(n)], int)

print(np.dot(a, b))
