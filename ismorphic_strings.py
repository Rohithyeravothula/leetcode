class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
        	return True
        tuples = list(set(zip(list(s), list(t))))
        tl = len(tuples)
        left = {x for (x,y) in tuples}
        right = {y for (x,y) in tuples}
        return tl == len(left) and tl == len(right)

s = Solution()
ss,t = "",""
print(s.isIsomorphic(ss, t))
