from collections import Counter
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jwels = set(J)
        ans = 0
        counter = Counter(S)
        for key in counter:
        	if key in jwels:
        		ans += counter[key]
        return ans


jj="aZ"
ss="AZ"
s=Solution()
print(s.numJewelsInStones(jj, ss))
