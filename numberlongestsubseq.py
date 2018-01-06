class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
        	return 0
        if l==1: 
        	return 1
        opt = [0]*l
        opt[0] = 1
        for i in range(1, l):
        	for j in range(0, i):
        		if nums[i] > nums[j]:
        			opt[i] = max(opt[i], opt[j])
        	opt[i]+=1

        print(opt)
        max_len = max(opt)
        if max_len == 1:
        	
        c = 0
        i = l-1
        while i>=0:
        	for j in range(0, i):
        		if opt[j] == max_len-1 and nums[j] < nums[i]:
        			c+=1
        	i-=1
        return c

# a=[1,3,5,4,7]
a=[5,4,3,2,1]
s=Solution()
print(s.findNumberOfLIS(a))