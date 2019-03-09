class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ans = []
        n = len(s)
        if numRows == 1 or numRows >= n:
        	return s

        i = 0
        
        while i<n:
        	ans.append(s[i])
        	i+=(2*(numRows)-2)
        i = 1
        while i<(numRows-1):
        	j=i
        	ans.append(s[j])
        	while True:
        		l1 = j+(2*(numRows)-2)
        		l2 = l1-2*i
        		if l1 >= n and l2 >= n:
        			break
        		if l2 < n: ans.append(s[l2])
        		if l1 < n: ans.append(s[l1])
        		j=l1
        	i+=1

        i = numRows-1
        while i<n:
        	ans.append(s[i])
        	i+=(2*(numRows)-2)
        return "".join(ans)

print(Solution().convert("abcde", 4))
