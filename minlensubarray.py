class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=1
        if s<0:
        	return 0
        l = len(nums)
        max_length = l+1
        cursum = nums[i]
        while i<=j or j<l:
        	if cursum >= s:
        		max_length = min(max_length, j-i)
        		cursum -= nums[i]
        		i+=1
        	elif j<l:
        		cursum += nums[j]
        		j+=1
        	else:
        		break
        if cursum >= s:
        	max_length = min(max_length, j-i)

        if max_length == l+1:
        	return 0
        return max_length

        

a=[2,90,1,1,10,50,50]
s=Solution()
print(s.minSubArrayLen(1000, a))