class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        opt = [0]*(n+1)
        opt[1] = 1
        if n==1:
        	return 1
        opt[2] = 1
        if n==2:
        	return 1
        opt[3]=1
        if n==3:
        	return 2
        for i in range(3, n+1):
        	for j in range(1, i):
        		opt[i] = max(i, max(opt[i], opt[j]*(i-j)))
        return opt[n]

s=Solution()
# print(s.integerBreak(0))
for i in range(1, 20):
	print(i, s.integerBreak(i))