class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 0
        if n==2:
            return 1
        opt = [2000]*(1+n)
        opt[0] = 0
        opt[1] = 1
        for i in range(2, n+1):
            if opt[i] == 2000: # i is prime
                opt[i] = i
            for j in range(2*i, n+1, i):
                opt[j] = min(opt[j], opt[i] + (j//i))
            # print(opt)
        return opt[n]


s=Solution()
print(s.minSteps(16))