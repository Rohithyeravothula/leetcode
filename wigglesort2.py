class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        l = len(nums)
        left = nums[:l//2]
        right = nums[l//2:][::-1]
        result = []
        for i,j in zip(left, right):
        	result.append(i)
        	result.append(j)
        if l%2:
        	result.append(nums[l//2])
        for i in range(0, l):
        	nums[i] = result[i]

s=Solution()
print(s.wiggleSort([1,2,2]))