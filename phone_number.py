
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        def build(cur):
        	if not cur:
        		return ['']

        	poss = d[cur[0]]
        	sol = build(cur[1:])
        	newsol = []
        	for s in sol:
        		for p in poss:
        			newsol.append(p+s)
        	return newsol
        return build(digits)

Solution().letterCombinations("2384726")



