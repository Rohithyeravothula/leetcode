def optimalUtlization(capacity, fgList, bgList):
    fgList.sort(key=lambda x:x[1])
    curmax = 0
    curans = []
    l = len(fgList)
    for bgi, bg in bgList:
        pfi, pfv = bin_search(fgList, l, capacity-bg)
        if not pfi:
            continue
        bgc = bg + pfv
        if bgc > curmax and bgc <= capacity:
            curmax = bgc
            curans = [(pfi, bgi)]
        elif bgc == curmax:
            curans.append((pfi, bgi))
    curans.sort()
    return curans

def Aircraft(forward, ret, maxValue):
        n = len(forward)
        m = len(ret)
        i = 0; j = m-1; ans = []
        temp = -1
        while i < n and j >= 0:
            #print (i , j)
            sumVal = forward[i][1] + ret[j][1]
            if temp < sumVal and sumVal <= maxValue:
                ans = []
                temp = sumVal
                ans.append((i+1, j+1))
                i += 1
            elif temp == sumVal and sumVal <= maxValue:
                ans.append((i+1, j+1))
                i += 1
            elif sumVal > maxValue:
                j -= 1
        return ans


cp = 7
fl = [[1,2], [2,4], [3,6]]
bl = [[1,2]]

cp = 10
bl = [[1,3],[2,3],[3,4],[4,5],[5,100]]
fl = [[1,3],[2,5],[3,7],[4,10]]

cp = 20
fl = [[1,8],[2,7],[3,14]]
bl = [[1,5],[2,10],[3,14]]


print(optimalUtlization(cp, fl, bl))
print(Aircraft(fl,bl,cp))
# bs = [1,2,3,4,6]
#print(bin_search(bs,len(bs),5))

"""

"""
