class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sl = len(s)
        tl = len(t)
        i=0
        j=0
        while i<sl and j<tl:
        	if s[i] == t[j]:
        		i+=1
        		j+=1
        	else:
        		j+=1
        if i==sl:
        	return True
        return False

s=Solution()
print(s.isSubsequence("", ""))