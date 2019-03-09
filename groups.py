from collections import Counter
class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        def gcd(x, y):
        	if x>y:
        		x,y = y,x
        	if x==y or x==0:
        		return y
        	return gcd(x, y%x)

        def gcd_list(a):
        	g = a[0]
        	for val in a[1:]:
        		g = gcd(g, val)
        	return g

        counter = list(Counter(deck).values())
        if not counter:
        	return False
        g = gcd_list(counter)
        if g<2:
        	return False
        return True

inp = [5,4,3,2]
print(Solution().hasGroupsSizeX(inp))