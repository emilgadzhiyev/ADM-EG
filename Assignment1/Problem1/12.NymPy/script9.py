# Min and Max

# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

N, M = map(int, input().split())

print(np.array([input().split() for _ in range(int(N))], int).min(1).max())
