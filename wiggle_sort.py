class Solution:
    def wiggleSort(self, a):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def get_crazy(c, cl):
        	if cl==1:
        		return c[0],None, None
        	elif cl==2:
        		return min(c), max(c), None
        	else:
        		cp = list(c)
        		c.sort()
        		m1,m3,m2 = c
        		return m1, m2, m3

        l = len(a)
        i = 0
        while i<l:
        	c = a[i:i+3]
        	cl = len(c)
        	m1,m2,m3 = get_crazy(c,cl)
        	if cl == 2:
        		a[i] = m1
        		a[i+1] = m2
        	elif cl == 3:
        		a[i] = m1
        		a[i+1] = m2
        		a[i+2] = m3
        	i+=2
        return a


inp = []
Solution().wiggleSort(inp)
print(inp)