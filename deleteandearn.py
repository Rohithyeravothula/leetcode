class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for i in nums:
        	if i in freq:
        		freq[i] += 1
        	else:
        		freq[i] = 1

        nums = list(set(nums))
        nums.sort()
        l = len(nums)
        opt = [0]*(l+1)
        for i in range(1, l+1):
        	if i>1 and nums[i-1] == nums[i-2]+1:
        		opt[i] = max(opt[i-2]+nums[i-1]*freq[nums[i-1]], opt[i-1])
        	else:
        		opt[i] = max(opt[i-1], opt[i-1] + nums[i-1]*freq[nums[i-1]])

        # print(opt)
        return opt[l]

a=[]
s=Solution()
print(s.deleteAndEarn(a))