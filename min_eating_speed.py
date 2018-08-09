from heapq import heappush, heappop, heapify
class Solution:
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        total = sum(piles)
        k = (total//h) + (total*())
        print(k)

        while True:
            cur = total//k
            for p in piles:
                if p%k!=0:
                    cur +=1
            print(cur, total, k)
            if cur == h:
                return k
            k+=1



s = Solution()
# pp = [332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673, 679580077, 337406589, 290818316, 877337160, 901728858, 679284947, 688210097, 692137887, 718203285, 629455728, 941802184]
# hh = 823855818
pp = [3,6,7,11]
hh = 8
print(s.minEatingSpeed(pp, hh))
