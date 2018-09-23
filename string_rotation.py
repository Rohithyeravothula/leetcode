class Solution:
    def orderlyQueue(self, s, k):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        l = len(s)
        if k==1:
        	a = []
        	for i in range(0, l):
        		a.append("".join(s[i:] + s[:i]))
        	a.sort()
        	return a[0]
        else:
        	s = list(s)
        	s.sort()
        	return "".join(s)

print(Solution().orderlyQueue("cba", 1))