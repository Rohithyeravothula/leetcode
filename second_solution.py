class Solution:
    def isRectangleOverlap(self, r1, r2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        def check(rec1, rec2):
            c1 = (rec1[0] >= rec2[0] and rec1[0] <= rec2[2]) or (rec1[2] >= rec2[0] and rec1[2] <= rec2[2])
            c2 = (rec1[1] >= rec2[1] and rec1[1] <= rec2[3]) or (rec1[3] >= rec2[1] and rec1[3] <= rec2[3])
            if c1 and c2:
            	return True
            return False
        if check(r1, r2) or check(r2, r1):
            return True
            