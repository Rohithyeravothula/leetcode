class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 0:
        	return [[]]
        l = len(s)
        sol = []
        for i in range(1, l+1):
        	if s[0:i] == s[0:i][::-1]:
        		ite = self.partition(s[i:])
        		for it in ite:
        			sol.append([s[0:i]] + it)
        return sol

a="abccc"
s=Solution()
print(s.partition(a))
