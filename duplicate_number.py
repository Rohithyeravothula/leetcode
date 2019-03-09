class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        prev = nums[0]
        i,l = 1, len(nums)
        while i<l and prev != nums[i]:
            prev = nums[i]
            i+=1
        return prev

s = Solution()
inp = [1,2,3,3,4]
print(s.findDuplicate(inp))