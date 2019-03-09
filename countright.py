from bisect import bisect_left, insort
class Solution:
    def countSmaller(self, nums: 'List[int]') -> 'List[int]':
    	if not nums:
    		return []
    	l = len(nums)
    	i = l-2
    	ans = [0]
    	right = [nums[-1]]
    	while i>=0:
    		a = bisect_left(right, nums[i])
    		ans.append(a)
    		insort(right, nums[i])
    		i-=1
    	return ans[::-1]

inp = [5,2,3,8]
inp = [5,2,6,1]
inp = [1,2,3,4]
inp = [2,1]
print(Solution().countSmaller(inp))        