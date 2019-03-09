from collections import Counter
class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dup, new, s = 0, 0, 0
        n = len(nums)
        for i in range(1, n+1):
            s += nums[i-1]
            dup = dup ^ nums[i-1] ^ i
        return [dup, ((n*(n+1))//2) - s]        
        

s = Solution()
inp = [5,3,2,1,6,6]
inp = [1,1]
print(s.findErrorNums(inp))