for _ in range(int(input())):
    n = int(input())
    arr = sorted([int(x) for x in input().split()])

    answer = 10000 
    for i in range(n-1):
        curr = arr[i+1] - arr[i]
        if curr < answer:
            answer = curr

    print(answer)