class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        class Point:
        	def __init__(self, x, y):
        		self.x = x
        		self.y = y

        	def __str__(self):
        		return "{},{}".format(self.x, self.y)


        def get_eq_coef(p1, p2):
        	m = (p2.y-p1.y)/(p2.x-p1.x)
        	c = p1.y - m*p1.x
        	return m, c

        def get_perp_coef(m, p1):
        	c = p1.y + m*p1.x
        	return -1*m, c

        def safe_remove(s, v):
        	if v in s:
        		s.remove(v)

        def get_next_point(m, c, p1):
        	points = {"0,0", "{},0".format(p), "{},{}".format(p, p), "0,{}".format(p)}
        	safe_remove("0,{}".format(p1.y))
        	safe_remove("{},0".format(p1.x))
        	safe_remove("{},{}".format(str(p1)))
        	valid_points = []
        	for pts in points:
        		x,y = map(int, pts.split(","))
        		if x == 0:
        			""
        		if y == 0:
        			""
        		if x == p:

        prev_point = Point(0,0)
        cur_point = Point(p,q)
        ans = ["{}0".format(p), "{}{}".format(p, p), "0{}".format(p)]
        while True:
        	m, c = get_eq_coef(prev_point, cur_point)
        	next_point = get_next_point(m, c, cur_point)

        	# ans check
        	if str(next_point) in ans:
        		return ans.indexof(str(next_point))



pp = 2
qq = 1
s = Solution()
s.mirrorReflection(pp, qq)