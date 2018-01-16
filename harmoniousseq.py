from collections import Counter
class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ctr = Counter(nums)
        ans = 0
        for k in ctr.keys():
	        if k+1 in ctr:
	        	ans = max(ans, ctr[k]+ctr[k+1])
        return ans

s=Solution()
print(s.findLHS([1,1,4,4,5]))
        