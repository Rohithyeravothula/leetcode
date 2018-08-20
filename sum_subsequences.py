class Solution:
    def sumSubseqWidths(self, a):
        """
        :type A: List[int]
        :rtype: int
        """
        p = (10**9) + 7
        l = len(a)
        a.sort()
        ans = 0
        for i, v in enumerate(a):
        	left = 1 << i
        	right = 1 << (l-i-1)
        	ans += (left - right) * v
        return ans % p

s = Solution()
print(s.sumSubseqWidths([4,5]))
[1,2,3]