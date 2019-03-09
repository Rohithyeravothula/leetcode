from collections import defaultdict
class Solution:
    def minDeletionSize(self, a):
        """
        :type A: List[str]
        :rtype: int
        """
        if not a:
        	return 0
        c = 0
        seen = defaultdict(int)
        l = len(a[0])
        indices = list(range(l))
        for s in a:
        	ci = []
        	for i in indices:
        		if ord(s[i]) > seen[i]:
        			seen[i] = ord(s[i])
        			ci.append(i)
        	indices = ci

        return l - len(indices)


inp = ["abc", "def"]
inp = []
inp = ["cba","daf","ghi"]
inp = ["zyx","wvu","tsr"]
inp = ["rrjk","furt","guzm"]
print(Solution().minDeletionSize(inp))


"""
rrjk
furt
guzm
04132
0123
3201
"""


        