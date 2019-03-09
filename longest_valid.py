class Solution:
    def longestValidParentheses(self, s: 'str') -> 'int':
        valid = set()
        stk = []
        ans = 0
        for i,c in enumerate(s):
        	if c=="(":
        		stk.append(i)
        	else:
        		if stk and s[stk[-1]] == "(":
        			valid.add(stk.pop())
        			valid.add(i)
        			prev = stk[-1] if stk else -1
        			ans = max(i-prev, ans)
        		else:
        			stk.append(i)
        return ans
        

inp = "()())()("
inp = "((()))))((()))()()()"
inp = "()((((())))"
inp = "(((((()()"
print(Solution().longestValidParentheses(inp))
