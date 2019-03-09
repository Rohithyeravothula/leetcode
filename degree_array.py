from collections import Counter
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return 0
        ans = len(nums)
        counts = Counter(nums).most_common()
        if len(counts) == ans:
        	return 1

        valid_entrees = {key: None for key, val in counts if val == counts[0][1]}
        for index, val in enumerate(nums):
        	if val in valid_entrees:
        		if valid_entrees[val] is None:
        			valid_entrees[val] = [index, index]
        		else:
        			valid_entrees[val][1] = index

        for val in valid_entrees:
        	si, ei = valid_entrees[val]
        	ans = min(ans, ei-si+1)

        return ans

s = Solution()
inp = []
inp = [1,2,2,4,5,5,2,2,3,3,3,0,0,0,0]
inp = [1,2,3,4,5,6,6]
print(s.findShortestSubArray(inp))
