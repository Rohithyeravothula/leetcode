class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<=1:
        	return x

        prev = 2
        diff = 1
        cur = 1
        while diff !=0:
        	prev = cur
        	cur = (prev+(x/prev))/2
        	diff = abs(cur-prev)
        	# print(cur)
        return int(cur)

s=Solution()
# print(s.mySqrt(2))
for i in range(0, 10):
	print(i,s.mySqrt(i))
