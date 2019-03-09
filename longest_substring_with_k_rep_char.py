class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for c in set(s):
            if s.count(c) < k:
                return max([self.longestSubstring(t, k) for t in s.split(c)])
        return len(s)


ss = Solution()
inp = "abc"
inp = "bbaaadc"
inp = "aacbbbdc"
print(ss.longestSubstring(inp, 2))



