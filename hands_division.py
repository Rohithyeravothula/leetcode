from collections import Counter
from heapq import heappush, heappop, heapify
class Solution:
    def isNStraightHand(self, hand, w):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        l = len(hand)
        if l%w != 0:
            return False
        counter = Counter(hand)
        hand_unique = list(set(hand))
        hand_unique.sort()
        cc = 0
        while hand_unique:
            start = hand_unique[0]
            if counter[start] == 0:
                hand_unique = hand_unique[1:] # replace with proper queue
            else:
                for i in range(0, w):
                    if counter[start+i] == 0:
                        return False
                    counter[start+i] -= 1
                cc += 1

        if cc == l//w:
            return True
        return False


info = [5,4,3,2,1,0]
s = Solution()
print(s.isNStraightHand(info, 5))

        