class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        idx = nums.index(m)
        del nums[idx]
        prop = True
        for i in nums:
            if 2*i > m:
                prop = False
                break
        if prop:
            return idx
        return -1

a=[1,2,3,4]
s=Solution()
print(s.dominantIndex(a))