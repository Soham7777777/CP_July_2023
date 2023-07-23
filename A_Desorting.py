for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]

    mn = 10000000001
    for i in range(n-1):
        if (diff := arr[i+1] - arr[i]) < mn:
            mn = diff
            if mn < 0:
                print(0)
                break
    else:
        print((mn//2)+1)