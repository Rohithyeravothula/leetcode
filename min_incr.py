from collections import Counter
class Solution(object):
    def minIncrementForUnique(self, a):
        """
        :type A: List[int]
        :rtype: int
        """
        if not a:
        	return 0
        counter = list(Counter(a).items())
        counter.sort()
        seen = set()
        mina = min(a)
        ans = 0
        for key, val in counter:
        	for cur in range(0, val):
        		while mina in seen:
        			mina += 1
        		mina = max(mina, key)
        		seen.add(mina)
        		ans += (mina - key)
        		mina += 1
        	# print(seen)
        return ans


inp = [1,2,2]
inp = [1,1,1]
inp = [3,2,1,2,1,7]
inp = [1,1,1,1,3]
inp = []
inp = [4,5,6]
print(Solution().minIncrementForUnique(inp))

        