from collections import Counter
class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        ls1 = len(s1)
        ls2 = len(s2)
        if ls1 > ls2:
        	return False
        s1a = [0]*26
        for i in s1:
        	s1a[ord(i) - ord('a')] += 1

       	s2a = [0]*26
        for i in range(0, ls1):
        	s2a[ord(s2[i]) - ord('a')] += 1

        if s1a == s2a:
        	return True

        for i in range(ls1, ls2):
        	last = s2[i-ls1]
        	cur = s2[i]
        	s2a[ord(last) - ord('a')] -= 1
        	s2a[ord(cur) - ord('a')] += 1
        	if s1a == s2a:
        		return True
        return False


s=Solution()
print(s.checkInclusion("a", ""))
        