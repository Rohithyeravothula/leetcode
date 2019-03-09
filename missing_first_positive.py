class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        start = 0
        end = l-1
        while start <= end:
            while start < l and nums[start] > 0:
                start += 1
            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
        for i in range(start):
            val = nums[i]
            idx = abs(val)-1
            if idx < start and nums[idx]>0:
                nums[idx] *= -1
        for i in range(start):
            if nums[i] > 0:
                return i+1
        return start+1

inp = [0,1,2]
inp = [-1,-2,-3]
inp = [1,-2,4,8,-2,0]
inp = [1,1]
inp = [1,2]
print(Solution().firstMissingPositive(inp))