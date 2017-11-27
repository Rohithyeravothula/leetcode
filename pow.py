class Solution:
    def power(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        elif n==1:
            return x
        
        t=self.power(x,int(n/2))
        if n%2==1:
            return t*t*x
        return t*t

    def myPow(self, x, n):
        ans = self.power(x,n)
        if n<0:
            return 1/ans
        return ans
            
s=Solution()
print(s.myPow(2.0, -4))