def bricksGame(arr):
    #
    # Write your code here.
    #
    arr = arr[::-1]
    l = len(arr)
    if l<4:
        return sum(arr)
    opt = [0]*(l+3)
    opt[3] = arr[0]
    opt[4] = arr[1] + opt[3]
    opt[5] = arr[2] + opt[4]
    for i in range(6, l+3):
        f1 = arr[i-3] + min([opt[i-2], opt[i-3], opt[i-4]])
        f2 = arr[i-3] + arr[i-4] + min([opt[i-3], opt[i-4], opt[i-5]])
        f3 = arr[i-3] + arr[i-4] + arr[i-5] + min([opt[i-4], opt[i-5], opt[i-6]])
        opt[i] = max([f1, f2, f3])
    # print(opt)
    # print(opt[l+2])
    return opt[l+2]

inp = [0,1,1,1,99]
bricksGame(inp)