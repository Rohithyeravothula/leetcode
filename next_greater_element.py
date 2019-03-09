from collections import OrderedDict 
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = OrderedDict({val:-1 for val in findNums})
        stk = []
        for val in nums:
        	while stk and val > stk[-1]:
        		cur = stk.pop()
        		if cur in seen:
        			seen[cur] = val
        	stk.append(val)
        return list(seen.values())

findNums, nums = [],[]
print(Solution().nextGreaterElement(findNums, nums))