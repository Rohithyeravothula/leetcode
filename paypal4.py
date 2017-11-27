def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def connectedCities(n, g, originCities, destinationCities):
    l=len(originCities)
    ans = []
    for i in range(0, l):
        if gcd(originCities[i], destinationCities[i]) > g:
            ans.append(1)
        else:
            add = 0
            m=min(originCities[i], destinationCities[i])
            maxdd=max(originCities[i], destinationCities[i])
            stk = [m]
            visited = {}
            visited[m] = 1
            while True:
                for i in range(m, n):
                    if len(stk) == 0:
                        break
                    p=stk.pop()
                    if i not in visited and gcd(p, i) > g:
                        if i == maxdd:
                            ans.append(1)
                            add = 1
                            break
                        stk.append(i)
                        visited[i] = 1
                if add == 1 and len(stk) ==0:
                    break
            if add == 0:
                ans.append(0)
    return ans


