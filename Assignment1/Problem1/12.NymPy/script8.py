# Sum and Prod

# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy

N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)], int)

print(numpy.prod(numpy.sum(A, axis=0), axis=0))
