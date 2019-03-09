class Solution:
    def circularArrayLoop(self, a: 'List[int]') -> 'bool':
        l = len(a)
        i = 0
        while i<l:
            if int(a[i]) == a[i]:
                factor = abs(a[i])/a[i]
                j = (i+a[i])%l
                a[i] += 0.5
                count = 1
                while True:
                    if factor*a[j] < 0:
                        break
                    elif int(a[j]) != a[j]:
                        if count > 1:
                            return True
                        else:
                            break
                    else:
                        curj = j
                        j = (j+a[j])%l
                        a[curj] += 0.5
                    count += 1
            i+=1
        return False
inp = [2, -1, 2, 2]
inp = [1,2,3,4]
inp = [-1, 2]
inp = [-2,1,-1,-2,-2]
inp = [2,4,5]
inp = []
inp = [-1, -2, -3]
print(Solution().circularArrayLoop(inp))
