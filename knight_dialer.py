class Solution:
    def knightDialer(self, n):
        """
        :type N: int
        :rtype: int
        """
        m = (10**9)+7
        a0,a1,a2,a4=1,1,1,1
        if n == 1:
            return 10

        for _ in range(1,n):
            c0 = (2*a4)%m
            c1 = (a2+a4)%m
            c2 = (2*a1)%m
            c4 = (2*a1 + a0)%m
            a0,a1,a2,a4 = c0,c1,c2,c4
        return (a0+(4*a1) + 2*a2 + 2*a4)%m

print(Solution().knightDialer(4))