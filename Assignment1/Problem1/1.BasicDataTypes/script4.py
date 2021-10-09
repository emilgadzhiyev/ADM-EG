# Lists

if __name__ == '__main__':
    N = int(input())
    L = []
    for _ in range(N):
        S = input().split()
        cmd = S[0]
        args = S[1:]
        if cmd != "print":
            cmd += "(" + ",".join(args) + ")"
            eval("L."+cmd)
        else:
            print(L)
