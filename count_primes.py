from math import sqrt
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = [1]*n
        a[0], a[1] = 0, 0
        l = int(sqrt(n)) + 1
        i = 2
        while i<=l:
            if a[i] == 1:
                j = 2*i
                while j<n:
                    a[j] = 0
                    j+=i
            i+=1
        return sum(a)

s = Solution()
print(s.countPrimes(30))


