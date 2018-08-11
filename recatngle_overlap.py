class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return not (rec1[2] <= rec2[0] or rec2[2] <= rec1[0] or rec1[3] <= rec2[0] or rec2[3] <= rec1[0])

r1 = [7,8,13,15]
r2 = [10,8,12,20]

s = Solution()
print(s.isRectangleOverlap(r1, r2))