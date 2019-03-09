class Solution:
    def maxTurbulenceSize(self, a):
        """
        :type A: List[int]
        :rtype: int
        """
        l = len(a)
        if l == 0:
        	return 0
        if len(set(a)) == 1:
        	return 1

        i = 2
        count = 2
        ans = 2
        while i<l:
        	p1 = a[i-1] - a[i-2]
        	p2 = a[i] - a[i-1]
        	if p1*p2 < 0:
        		count += 1
        		ans = max(ans, count)
        	else:
        		count = 2
        	i += 1
        return ans

s = Solution()
inp = [1,2,1,4,5]
inp = [9,4,2,10,7,8,8,1,9]
inp = [4,8,12,16]
inp = [1,2,1,2,1,2]
print(s.maxTurbulenceSize(inp))

        