class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = [-1, -1]
        l = len(nums)
        if l == 0:
            return ans
        i=0
        j=l-1
        while i<j:
            m=(i+j)//2
            if nums[m] < target:
                i=m+1
            else:
                j=m

        if nums[i] != target:
            return ans
        ans[0] = i
        j=l-1
        while i<j:
            m=1+((i+j)//2)
            if nums[m] > target:
                j=m-1
            else:
                i=m
        return [ans[0], j]

nums = [1,2,2,2,2,2,3,4]
target = 2
s=Solution()
print(s.searchRange(nums, target))

