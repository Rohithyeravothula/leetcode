class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l==0:
            return 0
        if l==1:
            return nums[0]
        opt = [0]*l
        opt = [max(opt[i-1], opt[i-2]+nums[i]) for i in range(2, l)]
        print(opt)
        return opt[l-3]

s = Solution()
print(s.rob([1,2,3,1]))
