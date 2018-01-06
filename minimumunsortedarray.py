class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        ordered = True
        for i in range(1, l):
            if nums[i] < nums[i-1]:
                ordered = False

        if ordered:
            return 0
        left = 0
        while left < l-1 and nums[left] <= nums[left+1]:
            left += 1

        right = l-1
        while right > 0 and nums[right] >= nums[right-1]:
            right -= 1

        umin = min(nums[left:right+1])
        umax = max(nums[left:right+1])

        start = 0
        while start < l and nums[start] <= umin:
            start += 1

        end = l-1
        while end >= 0 and nums[end] >= umax:
            end -= 1
        if start >= end:
            return 0
        return end-start+1


a=[2,1,3,0]
s=Solution()
print(s.findUnsortedSubarray(a))