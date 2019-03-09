class Solution:
    def rob(self, nums: 'List[int]') -> 'int':
        l = len(nums)
        opt = [0]*(l+1)
        for i in range(1, l+1):
        	opt[i] = max(opt[i-2]+nums[i-1], opt[i-1])
        return opt[-1]