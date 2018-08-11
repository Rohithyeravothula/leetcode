class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        def all_points(rec):
        	x1,y1,x2,y2 = rec
        	return [(x1,y1), (x1, y2), (x2, y1), (x2, y2)]

        rec2points = all_points(rec2)
        rec1points = all_points(rec1)

        rec1points.sort()
        rec2points.sort()

        if rec1points == rec2points:
        	return True

        x1,y1,x2,y2 = rec2
        for (x,y) in rec1points:
        	if x < x2 and x > x1 and y < y2 and y > y1:
        		return True
        return False

rec1 = [0,0,1,1]
rec2 = [1,0,2,1]

# rec1 = [1,1,3,3]
# rec2 = [3,3,1,1]

rec1 = [7,8,13,15]
rec2 = [10,8,12,20]

s = Solution()
print(s.isRectangleOverlap(rec1, rec2))