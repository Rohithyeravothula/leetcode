import operator as op
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        ops = {"*":op.mul, "/":op.floordiv, "+":op.add, "-":op.sub}
        stk = []
        l = len(s)
        i = 0
        while i<l:
        	j = i
        	while j<l and (s[j].isnumeric() or s[j] == " "):
        		j+=1
        	cur = int(s[i:j].strip())
        	
        	if not stk: 
        		stk.append(cur)
        	elif stk[-1] in {"*", "/"}:
        		curop = stk.pop()
        		prev = stk.pop()
        		stk.append(ops[curop](prev, cur))
        	else:
        		stk.append(cur)

        	if j<l and s[j] in ops:
        		stk.append(s[j])
        		j+=1
        	i = j
        l = len(stk)
        ans = stk[0]
        i = 1
        while i<l:
        	ans = ops[stk[i]](ans, stk[i+1])
        	i+=2
        return ans

print(Solution().calculate("2*3-10"))
