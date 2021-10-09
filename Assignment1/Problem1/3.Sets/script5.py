# Set .union() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
eng = set(map(int, input().split()))
b = input()
fre = set(map(int, input().split()))

print(len(eng.union(fre)))
