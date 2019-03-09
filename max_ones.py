def findMaxConsecutiveOnes(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    c = 0
    ans = 0
    for val in nums:
        c = (c+val)*val
        ans = max(ans, c)
    return ans

s = Solution()
inp = [1,0,1,1,0]
print(s.findMaxConsecutiveOnes(inp))
