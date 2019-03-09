def bin_search(a, k):
    if k<a[0]:
        return a[0]
    elif k>=a[-1]:
        return -1
    i,j = 0, len(a)-1
    response = None
    while i<j:
        m = i+(j-i)//2
        if a[m] == k:
            return a[m+1]
        elif a[m] < k:
            i=m+1
        else:
            response = a[m]
            j=m-1
    return response if k >= a[j] else a[j]

a = [2, 8, 14, 18, 25, 40]
k = 14
print(bin_search(a, k))
