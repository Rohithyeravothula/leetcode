class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        l = len(points)
        points = [(i, x, y) for i, (x, y) in enumerate(points)]
        busted = [0]*l
        start_times = [(i, x) for i, x, _ in points]
        end_times = [(i, y) for i, _, y in points]
        start_times.sort(key=lambda x: x[1])
        end_times.sort(key=lambda x: x[1])
        arrows = 0
        start_i = 0
        end_i = 0
        while start_i < l and end_i < l:
        	cur_end = end_times[end_i]
        	while start_i < l and start_times[start_i][1] <= end_times[end_i][1]:
        		busted[start_times[start_i][0]] = 1
        		start_i += 1
        	arrows += 1
        	# this should have been set in prev loop
        	busted[end_times[end_i][0]] = 1
        	end_i += 1
        	while end_i < l and busted[end_times[end_i][0]] == 1:
        		end_i += 1
        return arrows


# pts = [[10,16], [2,8], [1,6], [7,12]]
# pts = [[1,2],[2,3],[3,4],[4,5]]
# pts = [[1,2],[3,4], [4,8], [1, 20]]
pts = [[1,3], [3,5], [0, 20], [55,55]]
s = Solution()
print(s.findMinArrowShots(pts))