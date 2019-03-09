class Solution:
    def sortedSquares(self, a: 'List[int]') -> 'List[int]':
        def search_postive(a):
            l = len(a)
            i,j=0,l-1
            while i<j:
                m = i+(j-i)//2
                # print(i,j,m)
                if a[m] == 0:
                    return m
                elif a[m] > 0:
                    j-=1
                else:
                    i+=1
            return j

        if not a:
            return []
        l = len(a)
        if l==1:
            return [a[0]**2]
        result = []
        i = search_postive(a)
        j = i-1
        while j>=0 or i<l:
            left = a[j]*a[j] if j>=0 else float('inf')
            right = a[i]*a[i] if i<l else float('inf')
            if left < right:
                result.append(left)
                j-=1
            else:
                result.append(right)
                i+=1
        return result
inp = [-8,-4,-2,1,2,3,4]
print(Solution().sortedSquares(inp))


