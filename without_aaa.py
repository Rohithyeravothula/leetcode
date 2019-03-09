class Solution:
    def strWithout3a3b(self, a, b):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        c1, c2 = 'a', 'b'
        if a<b:
        	c1, c2 = 'b', 'a'
        	a,b = b,a
        ans = ""
        d = a-b
        for i in range(b):
        	if d>0:
        		ans += c1
        		d-=1
        	ans += (c1+c2)
        if a > 2*b:
        	ans += c1*(a-2*b)
        return ans


s = Solution()
print(s.strWithout3a3b(1,1))


        