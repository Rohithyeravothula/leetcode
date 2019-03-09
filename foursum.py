class Solution:
    def fourSum(self, a, t):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        a.sort()
        l = len(a)
        print(a)
        sol = []
        i=0
        while i<l:
            j=l-1
            while j>i:
                x=i+1
                y=j-1
                ps =  a[i] + a[j]
                while x<y:
                    # print(i,x,y,j)
                    s = ps + a[x] + a[y]
                    if s==t:
                        # print("strange", i,x,y,j)
                        sol.append([a[i], a[x], a[y], a[j]])
                        while (x+1) < y and a[x+1] == a[x]:
                            x+=1
                        while (y-1) > x and a[y-1] == a[y]:
                            y-=1
                        x+=1
                        y-=1
                    elif s<t:
                        while (x+1) < y and a[x+1] == a[x]:
                            x+=1
                        x+=1
                    else:
                        while (y-1) > x and a[y-1] == a[y]:
                            y-=1
                        y-=1
                while j>0 and a[j-1] == a[j]:
                    j-=1
                j-=1
            while (i+1) < l and a[i+1] == a[i]:
                i+=1
            i+=1
        return sol
inp,t = [1, 0, 0,-1, 2],0
inp,t = [-1,-5,-5,-3,2,5,0,4],-7
inp,t = [1, 0, -1, 0, -2, 2],0
print(Solution().fourSum(inp,t))
