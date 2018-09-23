class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        a = x >> 1
        b = 0.5
        count = 0
        while count < 100 and b != 0:
            # print(a, b)
            b = (x - (a*a))/(2*a)
            a += b
            count += 1
        return int(a)

print(Solution().mySqrt(1))