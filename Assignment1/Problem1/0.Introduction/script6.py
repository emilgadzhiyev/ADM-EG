# Print Function

if __name__ == '__main__':
    n = int(input())
    # Solution 0
    # if (n >= 1) and (n <= 150):
    #     for i in range(1, n + 1):
    #         if i == n:
    #             print(i)
    #         else:
    #             print(i, end='')
    # Soltion 1
    chain = ""
    if (n >= 1) and (n <= 150):
        for i in range(1, n + 1):
            chain += str(i)
        print(chain)
