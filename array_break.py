class Solution:
    def maxChunksToSorted(self, a):
        """
        :type arr: List[int]
        :rtype: int
        """
        l = len(a)
        i = 0
        ans = 0
        while i < l:
        	b = a[i]
        	while i <= b:
        		b = max(b, a[i])
        		i += 1
        	ans += 1
        return ans

s = Solution()
print(s.maxChunksToSorted([1,0,2,3,4]))
