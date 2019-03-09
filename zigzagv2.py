class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        l = len(s)
        if numRows >= l or not s or numRows == 1:
        	return s
        ans = [[] for _ in range(numRows)]
        cur, d = 0, 1
        i=0
        while i<l:
        	ans[cur].append(s[i])
        	if cur == 0:
        		d = 1
        	elif cur == numRows-1:
        		d = -1
        	i+=1
        	cur+=d
        ans = ["".join(val) for val in ans]
        return "".join(ans)

print(Solution().convert("AB", 1))