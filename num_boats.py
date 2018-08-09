from heapq import heapify, heappop, heappush
class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        if not people:
            return 0
        half = limit >> 1
        boats = 0
        if limit % 2 == 0:
            half_ppl = len([p for p in people if p == half])
            people = [p for p in people if p != half]
            boats = half_ppl >> 1
            if half_ppl % 2 == 1:
                people.append(half)

        half_less = [p for p in people if p <= half]
        half_more = [-1*p for p in people if p > half]
        heapify(half_more)
        half_less.sort()
        l = len(half_less)
        i = 0
        while i<l and half_more:
            cur = half_less[i]
            while half_more:
                p = -1*heappop(half_more)
                print(p, cur, i)
                if cur + p <= limit:
                    boats += 1
                    i += 1
                    break
                else:
                    boats += 1
                    break

        print(boats, half_more, i, l)
        boats += len(half_more)
        half_less_count = max(l-i, 0)
        boats += int(half_less_count/2 + half_less_count%2)
        return boats

inp = [5,1,4,2]
s = Solution()
print(s.numRescueBoats(inp, 6))
