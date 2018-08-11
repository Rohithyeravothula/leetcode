class Solution:
    def backspaceCompare(self, s, t):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def final(s):
        	a = []
        	for c in s:
        		if c == "#":
        			if a:
	        			a.pop()
        		else:
        			a.append(c)
        	return "".join(a)
        if final(s) == final(t):
        	return True
        return False

s = Solution()
print(s.backspaceCompare( "###", ""))

        