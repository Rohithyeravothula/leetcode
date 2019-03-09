from collections import Counter
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        counter = Counter(nums)
        uniques = list(counter.keys())
        def subset(nums, counter):
            if not nums:
                return [[]]
            cur = nums[0]
            rest = subset(nums[1:], counter)
            sol = []
            for pos in rest:
                sol.append(pos)
            
            for i in range(counter[cur]):
                for pos in rest:
                    sol.append(pos + [cur]*(i+1))
            return sol
        return subset(uniques, counter)

inp = [1,1,1]
print(Solution().subsetsWithDup(inp))

        