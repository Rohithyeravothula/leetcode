class Solution:
    def nextGreaterElements(self, nums: 'List[int]') -> 'List[int]':
        stk = []
        nums = nums + nums
        l = len(nums)
        l2 = l>>1
        ans = [-1]*l2
        for i in range(l):
        	while stk and nums[i] > nums[stk[-1]]:
        		j = stk.pop()
        		if j<l2:
        			ans[j] = nums[i]
        	stk.append(i)
        return ans

inp = [5]
print(Solution().nextGreaterElements(inp))