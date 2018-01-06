class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l == 0:
        	return 0
        if s==s[::-1]:
        	return len(s)
        opt = [[0]*l for _ in range(0, l)]
        for i in range(0, l):
        	opt[i][i] = 1

        for i in range(0, l-1):
        	opt[i][i+1] = 1
        	if s[i] == s[i+1]:
        		opt[i][i+1] = 2

        row = 0
        col = 2
        while row < l and col < l:
        	i = row
        	j = col
        	while i<l and j<l:
        		opt[i][j] = max(opt[i+1][j-1], max(opt[i][j-1], opt[i+1][j]))
        		if s[i] == s[j]:
        			opt[i][j] = max(2+opt[i+1][j-1], opt[i][j])
        		i+=1
        		j+=1
        	col+=1

        # for o in opt:
        # 	print(o)

        return opt[0][l-1]
s=Solution()
print(s.longestPalindromeSubseq(""))