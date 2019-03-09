class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses.sort(key = lambda x:x[1])
        m = 1
        prev_end = courses[0][1]
        for start, end in courses[1:]:
        	if prev_end < start:
        		m += 1
        		prev_end = end
        return m

inp = [[5,5],[4,6],[2,6]]
print(Solution().scheduleCourse(inp))