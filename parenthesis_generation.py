class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def build(lc, rc, cur):
            return [cur] if (lc==0 and rc==0) else ((build(lc-1, rc, cur+"(") if lc > 0 else []) + (build(lc, rc-1, cur+")") if lc < rc else []))
        return build(n,n,"")

print(Solution().generateParenthesis(-1))