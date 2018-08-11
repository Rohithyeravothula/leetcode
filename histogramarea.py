class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        def get_min_index(inp):
        	mini = 0
        	mine = inp[0]
        	l = len(inp)
        	for i in range(0, l):
        		if mine >= inp[i]:
        			mine = inp[i]
        			mini = i
        	return mini
        def get_area(inp):
        	if not inp:
        		return 0
        	elif len(inp) == 1:
        		return inp[0]
        	else:
	        	mini = get_min_index(inp)
	        	left = get_area(inp[:mini])
	        	right = get_area(inp[mini+1:])
	        	cur = len(inp)*inp[mini]
	        	return max([left, right, cur])
        return get_area(heights)

print(len(inpheights))
# s=Solution()
# print(s.largestRectangleArea(inpheights))
