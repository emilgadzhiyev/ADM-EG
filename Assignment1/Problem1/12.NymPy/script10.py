# Mean, Var, and Std

# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

n, m = [int(x) for x in input().strip().split()]
array = np.array(
    [[int(x) for x in input().strip().split()] for _ in range(n)], dtype=float
)

print(np.mean(array, axis=1))
print(np.var(array, axis=0))
print(round(np.std(array), 11))
