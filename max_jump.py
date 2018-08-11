class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_jump = nums[0]
        cur = 0
        l = len(nums)
        while cur < l and cur <= max_jump:
        	max_jump = max(cur + nums[cur], max_jump)
        	cur += 1

        if max_jump >= l-1:
        	return True

        return False


info = [1, 1, 3, 0, 0, 8]
s = Solution()
print(s.canJump(info))