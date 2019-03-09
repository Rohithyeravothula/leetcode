def unboundedKnapsack(k, arr):
    if not arr:
        return 0
    k+=1
    l = len(arr)
    opt = [[0]*k for _ in range(l)]
    for j in range(k):
        if arr[0] <= j:
            opt[0][j] = arr[0]
            
    for i in range(1, l):
        for j in range(k):
            opt[i][j] = opt[i-1][j]
            if arr[i] <= j:
                opt[i][j] = max(opt[i][j], arr[i] + opt[i-1][j-arr[i]])
    for row in opt:
        print(row)
    return opt[l-1][k-1]

# k,inp = 0, [1,2,34,5]
k,inp = 9, [3,4,4,4,8]
k,inp = 12, [9,6,1]
unboundedKnapsack(k, inp)