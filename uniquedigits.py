class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        def count(n):
            n = n-2
            ans = 81
            c=8
            while n!=0 and c!=0:
                ans = ans*c
                n = n-1
                c = c-1
            return ans
        n = min(10, n)
        a = [0]*(n+1)
        if n == 0:
            return 0
        elif n == 1:
            return 10
        a[1] = 10
        a[2] = 81
        for i in range(3, n+1):
            a[i] = count(i)
        return sum(a)

s=Solution()
print(s.countNumbersWithUniqueDigits(14))