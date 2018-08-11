from collections import Counter
from heapq import heappush, heappop
class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return S
        counter = Counter(S)
        max_val = max([c for _,c in counter.items()])
        counter = list(counter.items())
        counter = sorted(counter, key=lambda x: x[1], reverse=True)
        l = len(S)
        if max_val > (l/2) + (l%2):
            return ""
        ans = [""]*max_val
        index = 0
        # print(counter)
        for char, count in counter:
            for j in range(0, count):
                ans[index] += char
                index = (index + 1)%max_val
        return "".join(ans)




s = Solution()
print(s.reorganizeString("aab"))
