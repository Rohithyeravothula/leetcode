class Solution(object):
    def binaryGap(self, n):
        """
        :type N: int
        :rtype: int
        """
        max_dist = 0
        while n:
            # print(n)
            if n&1:
                n = n>>1
                c = 0
                while n:
                    if n&1:
                        break
                    n=n>>1
                    c+=1
                if n:
                    max_dist = max(max_dist, c+1)
            else:
                n=n>>1
        return max_dist
        

a=8
print(Solution().binaryGap(a), bin(a))