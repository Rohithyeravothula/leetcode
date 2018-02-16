class Solution:
    def twosumClosest(self, nums, target):
        l = len(nums)
        start = 0
        end = l-1
        ans = float("inf")
        while start<end:
            cursum = nums[start] + nums[end]
            if abs(target - cursum) < abs(target - ans):
                ans = cursum
            if cursum > target:
                end -= 1
            elif cursum < target:
                start += 1 
            elif cursum == target:
                return cursum
        return ans

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        nums.sort()
        ans = float("inf")
        for i in range(0, l):
            update = self.twosumClosest(nums[i+1:], target-nums[i])
            if abs(target - update - nums[i]) < abs(ans - target):
                ans = update+nums[i]
        return ans



art = [0, 0, 199]
s=Solution()
print(s.threeSumClosest(art, 100))