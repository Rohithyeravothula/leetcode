class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        def get_valid_strings(inp):
        	if not inp:
        		return []
        	if len(inp) == 2:
        		return [inp]
        	cl, cr = 0, 0
        	for i,v in enumerate(inp):
        		if v == "(":
        			cl += 1
        		elif v == ")":
        			cr += 1
        		if cl == cr:
        			break
        	cur_vs = [inp[:i+1]]
        	next_vs = get_valid_strings(inp[i+1:])
        	cur_vs.extend(next_vs)
        	return cur_vs


        def score_paran(S):
        	if not S:
        		return 0
        	if S=="()":
        		return 1
        	vss = get_valid_strings(S)
        	# print(S, vss)
        	# print(vss)
        	score = 0
        	for vs in vss:
        		if vs == "()":
        			score += 1
        		else:
	        		score += 2*score_paran(vs[1:-1])
        	return score

        return score_paran(S)





s = Solution()
print(s.scoreOfParentheses("(()())()(()(()())())"))
# 
