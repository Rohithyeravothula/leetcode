class Solution(object):
    def bagOfTokensScore(self, a, p):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        if not a:
            return 0
        a.sort()
        l=len(a)
        ans = 0
        i,j,points = 0,l-1,0
        while i<=j:
            # print(i,j,p)
            if a[i] <= p:
                p-=a[i]
                i+=1
                points += 1
                ans = max(points, ans)
            else:
                if points>0:
                    p+=a[j]
                    j-=1
                    points -= 1
                else:
                    break
        return ans
            



inp,p = [100,200,300,400],300
inp,p = [10,20,30],60
inp,p = [10,20,30,40,50],1000
inp,p = [100, 200, 300, 400], 200
inp,p = [1,28,29,30],2
inp,p = [100,200,300],20
print(Solution().bagOfTokensScore(inp,p))



"""
"""