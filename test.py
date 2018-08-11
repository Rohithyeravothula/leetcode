def largest_small(a, v, l):
    i = 0
    j = l-1
    if a[j] < v:
        return j 
    if a[i] > v:
        return -1

    ans = -1
    while i<j:
        m = (i+j)//2
        # print(i, j, m)
        if a[m] == v:
            return m 
        elif a[m] < v:
            i = m+1
            ans = m
        else:
            j = m-1
    if i == j and a[i] <= v:
        ans = i
    return ans


bb = [2, 4, 6, 8, 10]
print(largest_small(bb, 4, len(bb)))
# for i in range(0, 11):
#     print(i, largest_small(bb, i, len(bb)))