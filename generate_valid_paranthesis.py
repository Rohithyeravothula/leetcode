class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(cur, oc, cc, ans):
        	if oc == 0:
        		ans.append(cur + ")"*cc)
        	elif oc <= cc:
        		generate(cur + "(", oc-1, cc, ans)
        		generate(cur + ")", oc, cc-1, ans)
        response = []
        generate("", n, n, response)
        return response

s = Solution()
for i in range(1, 20):
	print(i, len(s.generateParenthesis(i)))

