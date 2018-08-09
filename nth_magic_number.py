
class Solution(object):
    def nthMagicalNumber(self, n, a, b):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        def get_gcd(a,b):
            if a>b:
                a,b = b,a
            if a==b:
                return a
            elif a==1:
                return 1
            return get_gcd(a, b-a)
        mod = (10**9) + 7
        lcm = (a*b)/get_gcd(a,b)
        l = min(a, b)
        r = min(a, b)*n
        while True:
            m = (l+r) >> 1
            val = (m//a) + (m//b) - (m//lcm)
            if val == n:
                return max((m//a)*a, (m//b)*b) %  mod
            elif val > n:
                r = m-1
            else:
                l = m+1

N,A,B=3,2,3
s = Solution()
print(s.nthMagicalNumber(N, A, B))
