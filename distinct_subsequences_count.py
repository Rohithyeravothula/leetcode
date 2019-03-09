from collections import defaultdict
class Solution:
    def distinctSubseqII(self, s):
        """
        :type S: str
        :rtype: int
        """
        m=int(1e9+7)
        seen = defaultdict(list)
        ans = 0
        for idx, val in enumerate(s):
        	if val not in seen:
        		ans = (2*ans + 1)%m
        		seen[val].append(idx)
        	else:
        		seen[val].append(idx)
        		prev = 0
        		for i in seen[val]:
        			d = i-prev
        			ans += ((d*(d+1))/2)%m
        			prev = i
        		ans += 1
        return ans%m

        

inp = ""
inp = "abca"
inp = "abc"
inp = "aaa"
inp = "aba"
inp = "baa"
inp = "babb"
print(Solution().distinctSubseqII(inp))
        