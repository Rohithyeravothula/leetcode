def maxsumsbuseq():
    t=int(input())
    for tt in range(0, t):
        n = int(input())
        if n == 0:
            return 0
        a = list(map(int, input().split()))
        opt = [0] * (1+n)
        opt[1] = a[0]
        for i in range(2, n+1):
            opt[i] = max([opt[i-2]+a[i-1], a[i-1], opt[i-1], opt[i-2]])
            # print(opt)
        return opt[n]

print(maxsumsbuseq())