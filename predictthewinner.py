class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        if l==0:
        	return False
        if l==1:
        	return True
        opt = [[0] * l for _ in range(0, l)]
        for i in range(0, l):
        	opt[i][i] = nums[i]

        for i in range(0, l-1):
        	opt[i][i+1] = nums[i]
        	if nums[i+1] > nums[i]:
        		opt[i][i+1] = nums[i+1]

        col = 2
        while col < l:
        	i = 0
        	j = col
        	while j<l:
        		first = nums[i] + min(opt[i+2][j], opt[i+1][j-1])
        		second = nums[j] + min(opt[i+1][j-1], opt[i][j-2])
        		opt[i][j] = max(first, second)
        		j+=1
        		i+=1
        	col+=1
        for o in opt:
        	print(o)
        print(opt[0][l-1])
        if opt[0][l-1] > sum(nums)-opt[0][l-1]:
        	return True
        return False

nms=[1,2,3,4,5]
s=Solution()
s.PredictTheWinner(nms)