class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l==0:
        	return 0
        maxa = [0]*l 
        mina = [0]*l
        maxa[0] = nums[0]
        mina[0] = nums[0]
        for i in range(1, l):
        	candidates = [maxa[i-1]*nums[i], mina[i-1]*nums[i], nums[i]]
        	maxa[i] = max(candidates)
        	mina[i] = min(candidates)
        return max(maxa)

aa=[]
s=Solution()
print(s.maxProduct(aa))