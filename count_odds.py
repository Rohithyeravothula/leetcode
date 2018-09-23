def count_odd(a, k):
    l = len(a)
    prefix = [0]*l
    odd = 0
    ans = 0
    for i in range(l):
        prefix[odd] += 1
        if a[i] & 1:
            odd+=1
        if odd > k:
            ans += prefix[odd-k]
    print(prefix)
    print(ans)

count_odd([2,1,4,1], 0)