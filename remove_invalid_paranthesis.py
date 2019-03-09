class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l = len(s)
        d = []
        for idx,val in enumerate(s):
        	if val == "(":
        		d.append(idx)
        	elif val == ")":
        		if not d:
        			d.append(idx)
        		else:
        			if s[d[-1]] == "(":
        				d.pop()
        			else:
        				d.append(idx)
        d = list(set(d))



inp = ""
print(Solution().removeInvalidParentheses(inp))
