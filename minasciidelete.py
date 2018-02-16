class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        l = len(s1)
        b = len(s2)
        opt = [[0] * (b+1) for _ in range(0, l+1)]
        for i in range(1, l+1):
        	opt[i][0] = opt[i-1][0]+ord(s1[i-1])

        for j in range(1, b+1):
        	opt[0][j] = opt[0][j-1]+ord(s2[j-1])

        for i in range(1, l+1):
        	for j in range(1, b+1):
        		if s1[i-1] == s2[j-1]:
        			opt[i][j] = opt[i-1][j-1]
        		else:
        			opt[i][j] = min(opt[i-1][j]+ord(s1[i-1]), opt[i][j-1]+ord(s2[j-1]))
        return opt[l][b]

s=Solution()
print(s.minimumDeleteSum("a", "aaa"))