import math
class Solution(object):
    def countPrimes(self, number):
        """
        :type n: int
        :rtype: int
        """
        def ch(n):
            if n <= 1:
                return False
            if n==2 or n==3:
                return True
            r = int(math.sqrt(n)) + 1
            is_prime = True
            for i in range(2, r):
                if n%i == 0:
                    is_prime = False
                    break
            return is_prime
        if number <=1:
            return 0
        elif number <= 3:
            return 1
        elif number <= 5:
            return 2
        c=2
        i = 5
        while i<number:
            if ch(i):
                c+=1
            i+=2
        return c

s=Solution()
for i in range(1, 10):
    print(i, s.countPrimes(i))