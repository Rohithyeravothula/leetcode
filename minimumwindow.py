from collections import Counter
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s or len(s) < len(t):
            return ""
        chars = set(t)
        base_freq = Counter(t)
        freq = Counter()
        curchar = set(t)
        l = len(s)
        for i in range(0,l):
            if s[i] in curchar:
                curchar.remove(s[i])
            if s[i] in chars:
                freq[s[i]] += 1
            if not curchar:
                break
        min_window = s[:i+1]
        min_window_length = i+1
        i+=1
        j = 0
        while i < l:
            if s[i] in chars:
                freq[s[i]] += 1
            while j < i:
                if s[j] in chars and freq[s[j]] > base_freq[s[j]]:
                    freq[s[j]] -= 1
                    j += 1
                if s[j] not in chars:
                    j += 1
                else:
                    break

            if i-j+1 < min_window_length:
                min_window = s[j:i+1]
                min_window_length = i-j+1
            i+=1
        return min_window

s=Solution()
print(s.minWindow("aaaa", "aa"))


