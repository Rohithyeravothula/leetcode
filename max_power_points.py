class Solution(object):
    def bagOfTokensScore(self, a, p):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        a.sort()
        l = len(a)
        if p<min(a):
        	return 0
        i,j=0,l-1
        ans = 0
        while i<=j:

        	while p >= a[i]:
        		p -= a[i]
        		i+=1
        		ans += 1
        	print(i,j,p,ans)
        	if i>=j:
        		break
        	p += a[j]
        	j-=1
        return ans

inp,p = [1,28,29,30],2
inp,p = [100,200,300,400],200
print(Solution().bagOfTokensScore(inp,p))

        