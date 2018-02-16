from collections import Counter
from heapq import heappush, heappop
class Solution:
    def reorganizeString(self, input_string):
        """
        :type S: str
        :rtype: str
        """
        l = len(input_string)
        t = l//2 + l%2
        counter = Counter(input_string)
        freq = []
        for key in counter:
            if counter[key] > t:
                return ""
        for key in counter:
            heappush(freq, (-1*counter[key], counter[key], key))


        ans = ""
        while freq:
            p1, c1, a1 = heappop(freq)
            if freq:
                p2, c2, a2 = heappop(freq)
                cand = a1+a2
                cand = cand*c2
                ans = ans + cand
                p3 = (c1-c2)
                if c1!=c2:
                    heappush(freq, (-1*p3, p3, a1))
            else:
                ans = ans + c1*a1
        return ans

s=Solution()
print(s.reorganizeString("pppp"))


        



