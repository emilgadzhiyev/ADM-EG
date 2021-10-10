# Shape and Reshape

# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

a = np.array(list(map(int, input().split())))
a.shape = (3, 3)

print(a)
