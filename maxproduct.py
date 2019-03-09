from heapq import nlargest, nsmallest
class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1, m2, m3 = nlargest(3, nums)
        s1, s2 = nsmallest(2, nums)
        return max(m1*m2*m3, s1*s2*m1)


inp = [-4,-3,1,2,3,4,5]
s = Solution()
print(s.maximumProduct(inp))
        