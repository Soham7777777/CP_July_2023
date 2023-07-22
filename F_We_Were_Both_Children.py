# for _ in range(int(input())):
#     n = int(input())
#     arr = sorted([int(x) for x in input().split()])
#     frequencies = [0]*(n+1)

#     cnt,i,rng = 1,0,n-1
#     while i < rng:
#         while i < rng and arr[i] == arr[i+1]:
#             cnt += 1
#             i += 1
        
#         jump = arr[i]
#         while jump <= n:
#             frequencies[jump] += cnt
#             jump += arr[i]
            
#         if i == rng:  # condition will be true when last element occures more than one time
#             break

#         cnt = 1
#         i+=1

#     else: # condition will be true when last element will occur only once
#         jump = arr[i]
#         while jump <= n:
#             frequencies[jump] += cnt
#             jump += jump
    
#     print(max(frequencies))



for _ in range(int(input())):
    n = int(input())
    hop_frog_map = [0]*(n+1)
    for elem in input().split():
        if int(elem) <= n:
            hop_frog_map[int(elem)] += 1

    # simulate frogs 
    jump_data = [0]*(n+1)
    for hop,frogs in enumerate(hop_frog_map[1:]):
            for i in range(hop+1,n+1,(hop+1)):
                jump_data[i] += frogs

    print(max(jump_data))

# take away: you do not have to directly input everything, you can do other things while taking input as well, just like here we mapped the hops of frogs to frog numbers and taking filterd input as well.