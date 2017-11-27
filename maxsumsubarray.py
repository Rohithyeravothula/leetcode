class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        prev = nums[0]
        maxSum = prev
        for i in range(1, l):
            curSum = max(prev+nums[i], nums[i])
            if curSum < maxSum:
                maxSum = curSum
            prev = curSum
            print(prev)
        return maxSum


a=[-2,1,-3,4,-1,2,1,-5,4]
s=Solution()
s.maxSubArray(a)