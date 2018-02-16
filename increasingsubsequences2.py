class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for i in nums:
        	dummy = [[i]]
        	for a in ans:
        		if a and a[-1] <= i:
        			dummy.append(a+[i])
        	ans.extend(dummy)
        return ans
s=Solution()
print(s.findSubsequences([4,5,7,7]))


"""
4,5,5 => 4 + (5,5)
"""