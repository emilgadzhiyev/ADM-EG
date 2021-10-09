# Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # Solution below
    # arr = list(arr)
    # if ((n >= 2) and (n <= 10)):
    #     flag = False
    #     for i in arr:
    #         if ((i <= -100) and (i <= 100)):
    #             flag = True
    #             break
    #     if (flag == False):
    #         maxNum = arr[0]
    #         for i in arr:
    #             if (maxNum < i):
    #                 maxNum = i
    #         # print(maxNum)
    #         try:
    #             while True:
    #                 arr.remove(maxNum)
    #         except ValueError:
    #                 pass
    #         # print(arr)
    #         maxNum = arr[0]
    #         for i in arr:
    #             if (maxNum < i):
    #                 maxNum = i
    #     print(maxNum)

    def findMax(num_list):
        maxNum = num_list[0]
        for i in num_list:
            if (maxNum < i):
                maxNum = i
        return maxNum
    arr = list(arr)
    if ((n >= 2) and (n <= 10)):
        flag = False
        for i in arr:
            if ((i <= -100) and (i <= 100)):
                flag = True
                break
        if (flag == False):
            maxNum = findMax(arr)
            arr.remove(maxNum)
            runnerUp = findMax(arr)
            while(runnerUp == maxNum):
                runnerUp = findMax(arr)
                arr.remove(runnerUp)
    print(runnerUp)
