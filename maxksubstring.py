from collections import Counter
class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = len(s)
        if l < k:
        	return 0
        counter = Counter(s)
        minc = min(counter, key=counter.get)
        if counter[minc] >= k:
        	return l
        for i in range(0, l):
        	if s[i] == minc:
        		break
        return max(self.longestSubstring(s[0:i], k), self.longestSubstring(s[i+1:], k))

s=Solution()
print(s.longestSubstring("ababbc", 1))