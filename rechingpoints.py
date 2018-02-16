class Solution:
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        def gcd(x,y):
            if x==0:
                return y
            if y==0:
                return x
            elif x<y:
                return gcd(x, y%x)
            else:
                return gcd(x%y, y)

        if gcd(sx, sy) == gcd(tx, ty):
            return True
        return False

s=Solution()
print(s.reachingPoints(1,8,4,15))
