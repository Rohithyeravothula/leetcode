class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def build(a, j, l):
        	if j==l-1:
        		return [[a[j]]]
        	result = []
        	for i in range(j, l):
        		a[j], a[i] = a[i], a[j] # swaping 
        		local = build(a, j+1, l)
        		for seq in local:
        			seq.append(a[j])
        			result.append(seq[::-1])
        		a[j], a[i] = a[i], a[j]
        	return result
        l = len(nums)
        return build(nums, 0, l)

inp = [3]
inp = [1,2,3]
print(Solution().permute(inp))
