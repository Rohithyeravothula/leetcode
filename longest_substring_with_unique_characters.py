class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        i = 0
        j = 0
        seen = set()
        maxl = 0
        while i<l:
        	while j<l and s[j] not in seen:
        		seen.add(s[j])
        		j+=1
        	maxl = max(maxl, j-i)
        	if j>=l:
        		break
        	seen_char = s[j]
        	# print(i, j)
        	while i<l and s[i]!=seen_char:
        		seen.remove(s[i])
        		i+=1
        	seen.remove(seen_char)
        	i+=1
        return maxl

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
