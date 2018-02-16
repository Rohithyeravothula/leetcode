from collections import Counter
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d=Counter(s)
        ans = 0
        c=0
        for i in d:
        	if d[i] > 1:
        		ans = ans + ((d[i]//2)*2)
        		d[i] = d[i]%2
        		if d[i]:
        			c=1
        	if d[i] == 1:
        		c=1
        return c+ans
s=Solution()
print(s.longestPalindrome(""))