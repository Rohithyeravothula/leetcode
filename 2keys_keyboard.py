from math import sqrt
class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        def get_factors(n):
            factors = set()
            m = int(sqrt(n)) + 1
            for i in range(2, m):
                if n%i==0:
                    factors.add((i, n//i))
                    factors.add((n//i, i))
            return list(factors)


        opt = [0]*(n+1)
        opt[0] = 0
        opt[1] = 0
        for i in range(2, n+1):
            min_val = i
            for a, b in get_factors(i):
                print(i, a, b, opt[i//a], a)
                cur_val = opt[i//a] + a
                if cur_val < min_val:
                    min_val = cur_val
            opt[i] = min_val
        return opt[n]
s = Solution()
print(s.minSteps(48))
