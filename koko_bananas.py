import math
class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        def get_time(a, r):
        	return sum([math.ceil(i/r) for  i in a])

        start = 1
        end = max(piles)
        minK = max(piles)
        while start <= end:
        	rate = (start + end) >> 1
        	time = get_time(piles, rate)
        	if time > H:
        		start = rate+1
        	else:
        		end = rate-1
        return start

s = Solution()
print(s.minEatingSpeed([332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673, 679580077, 337406589, 290818316, 877337160, 901728858, 679284947, 688210097, 692137887, 718203285, 629455728, 941802184],823855818))
