class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        opt = [0]*l
        opt[0] = nums[0]
        for i in range(1, l):
            opt[i] = max(opt[i-1]+nums[i], nums[i])
        return max(opt)

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
