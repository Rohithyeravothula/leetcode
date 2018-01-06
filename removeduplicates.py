class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        replace = 0
        l = len(nums)
        while i<l:
        	j=i+1
        	while j<l and nums[i] == nums[j]:
        		j+=1
        	r=j-1
        	nums[replace] = nums[r]
        	i=j
        	replace += 1
        return replace

a=[]
s=Solution()
m = s.removeDuplicates(a)
print(a[:m])