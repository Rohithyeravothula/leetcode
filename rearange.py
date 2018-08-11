from collections import Counter
from heapq import heappush, heappop
class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        counter = Counter(S)
        l = len(S)
        h = []
        for c,v in counter.items():
            if v > (l/2) + (l%2):
                return ""
            heappush(h, (-1*v,c))
        ans = ""
        while h:
            if len(h) == 1:
                _, cur_char = heappop(h)
                return ans + cur_char
            cur_count, cur_char = heappop(h)
            next_count, next_char = heappop(h)
            ans += cur_char + next_char
            if cur_count < -1:
                heappush(h, (cur_count+1, cur_char))

            if next_count < -1:
                heappush(h, (next_count+1, next_char))
        return ans


s = Solution()
print(s.reorganizeString("aaaaybdf"))
