from typing import List

from collections import Counter, defaultdict
class Solution:
    def commonChars(self, a: List[str]) -> List[str]:
        if not a:
            return []
        min_freq = {}
        orda = ord('a')
        seen = [0]*26
        for ch in a[0]:
            seen[ord(ch) - orda] = 1
        allch = [chr(i+orda) for i in range(26)]
        for word in a:
            wc = Counter(word)
            for key, val in wc.items():
                if key not in min_freq:
                    min_freq[key] = val
                else:
                    min_freq[key] = min(min_freq[key], val)
            for ch in allch:
                if ch not in wc:
                    seen[ord(ch) - orda] = 0
        ans = []
        for i, ch in enumerate(allch):
            if seen[i] == 1:
                char = chr(orda + i)
                ans.extend([char]*min_freq[char])
        return ans

inp = ["abc", "cab", "ba"]
print(Solution().commonChars(inp))
