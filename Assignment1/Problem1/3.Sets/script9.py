# Set Mutations

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
a = set(map(int, input().split()))
N = int(input())

for i in range(N):
    cmd = input().split()
    opt = cmd[0]
    s = set(map(int, input().split()))
    if (opt == 'update'):
        a |= s
    elif (opt == 'intersection_update'):
        a &= s
    elif (opt == 'difference_update'):
        a -= s
    elif (opt == 'symmetric_difference_update'):
        a ^= s

print(sum(a))
