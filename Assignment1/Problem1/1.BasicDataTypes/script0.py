# List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # Solution below
    arr = []
    for i in range(0, x+1):
        # print("x" + str(x))
        for j in range(0, y+1):
            # print("x" + str(x) + "y" + str(y))
            for k in range(0, z+1):
                #print("x" + str(x) + "y" + str(y) + "z" + str(z))
                if ((i + j + k) != n):
                    arr.append([i, j, k])
    print(arr)
