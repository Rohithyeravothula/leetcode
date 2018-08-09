class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        updated = []
        ends = []
        for start, end in points:
            updated.append((start, end))
            ends.append((end, start))
        updated.sort()
        ends.sort()
        marker = {}
        for tup im updated:
            marker[tup] = 0

        count = 0
        for start, end in ends:
            if marker[(start, end)] == 1:
                continue
            
