class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        i = 0
        while i<=32:
        	ones = 0
        	for num in nums:
        		ones += (num >> i)&1
        	b = 1 if ones%3==1 else 0
        	ans = b<<i | ans
        	i+=1
        return ans

s = Solution()
inp = [2,3,2,2,4,4,4]
inp = [0,1,0,1,0,1,99]
print(s.singleNumber(inp))

