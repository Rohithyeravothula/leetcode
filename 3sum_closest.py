class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        l = len(nums)
        i = 0
        closest = float("inf")
        while i < l:
        	j = i+1
        	k = l-1
        	while j<k:
        		cur_sum = nums[i] + nums[j] + nums[k]
        		cur_diff = abs(target - cur_sum)
        		closest_diff = abs(target - closest)
        		if cur_diff < closest_diff:
        			closest = cur_sum
        		if cur_sum > target:
        			k -= 1
        		else:
        			j += 1
        	i += 1
        return closest


ary = [-1, 2, 1, -4]
trg = 1
s = Solution()
print(s.threeSumClosest(ary, trg))

        		

