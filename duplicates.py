class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dup = []
        l = len(nums)
        for i in range(0, l):
            if nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
        for i in range(0, l):
            if nums[i] > 0:
                dup.append(i+1)

        return dup

a=[1,2,2,3,4,4]
s = Solution()
print(s.findDuplicates(a))