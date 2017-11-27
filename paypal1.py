def degreeOfArray(arr):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1
    maxD = 0
    maxI = -1
    for i in d:
        if d[i] > maxD:
            maxD = d[i]
            maxI = i
    cand = []
    for i in d:
        if d[i] == maxD:
            cand.append([maxD, i])

    l=len(arr)
    minL = l
    for c in cand:
        maxI = c[1]
        for i in range(0, l):
            if arr[i] == maxI:
                s=i
                break
        for i in range(0, l):
            if arr[l-i-1] == maxI:
                e=l-i-1
                break
        if minL > (e-s+1):
            minL = e-s+1
    return minL


a=[1,2,2,3,1]
print(degreeOfArray(a))