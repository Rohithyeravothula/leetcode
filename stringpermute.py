class Solution:
    def letterCasePermutation(self, S):
    	if len(S) == 0:
    		return [""]
    	else:
    		return self.helper(list(S))
    def helper(self, lst):
        """
        :type S: str
        :rtype: List[str]
        """
        if len(lst) == 1:
        	if lst[0].isalpha():
        		return [lst[0].lower(), lst[0].upper()]
        	else:
        		return [lst[0]]
        else:
        	cur = lst[0]
        	sol = []
        	prev = self.letterCasePermutation(lst[1:])
        	if cur.isalpha():
	        	for p in prev:
	        		sol.append(cur.lower() + p)
	        		sol.append(cur.upper() + p)
	        else:
	        	for p in prev:
	        		sol.append(cur+p)
        	return sol

s=Solution()
ans = s.letterCasePermutation("1")
print(len(ans), ans)
