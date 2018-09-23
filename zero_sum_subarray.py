class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums = [-1 if num == 0 else 1 for num in nums]
        l = len(nums)
        pre_sum = [0]*l
        pre_sum[0] = nums[0]
        for i in range(l-1):
            pre_sum[i+1] = pre_sum[i]+nums[i+1]

        print(pre_sum)
        seen = {}
        ml = 0
        for index, val in enumerate(pre_sum):
            if val == 0:
                ml = max(ml, index+1)
            elif val in seen:
                ml = max(ml, index - seen[val])
            else:
                seen[val] = index
        return ml

s = Solution()
print(s.findMaxLength([1,0, 0, 1]))