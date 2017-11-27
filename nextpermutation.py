class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = None
        l = len(nums)
        for i in range(0, l-1):
        	if nums[i] < nums[i+1]:
        		n = i
        if n is None:
        	nums.sort()
        else:
        	peak = nums[n+1]
        	right_min = n+1
        	for i in range(n+1, l):
        		if nums[i] > nums[n] and nums[right_min] > nums[i]:
        			right_min = i
        	nums[n], nums[right_min] = nums[right_min], nums[n]
        	nums[n+1:] = sorted(nums[n+1:])

a = list("54321")
s = Solution()
s.nextPermutation(a)
print(a)

