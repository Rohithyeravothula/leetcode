class Solution:
    def removeInvalidParentheses(self, s: 'str') -> 'List[str]':
        def remove(s):
        	ans = set()
        	l = len(s)
        	i = 0
        	while i<l:
        		if s[i] == ")":
        			ans.add(s[:i] + s[i+1:])
        		i+=1
        	return ans

        l = len(s)
        i=0
        count = 0
        ans = set()
        prev = 0
        while i<l:
        	if s[i] == "(":
        		count += 1
        	elif s[i] == ")":
        		count -= 1
        	if count == -1:
        		cur = remove(s[prev:i+1])
        		updated = set()
        		for old in ans:
        			for pos in cur:
	        			updated.add(old+pos)
	        	ans = updated
	        	prev = i+1
        	i+=1

print(Solution().removeInvalidParentheses("()())()())"))
