class Solution:
    def checkGood(self, n):
        rotate = {0:0, 1:1, 2:5, 5:2, 6:9, 8:8, 9:6}
        new = ""
        nlist = list(str(n))
        for i in nlist:
            if int(i) not in rotate:
                return False
            new += str(rotate[int(i)])
        new = int("".join(new))
        # print(new, n)
        if new == n:
            return False
        # print(new, n)
        return True
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        c=0
        for i in range(1, N+1):
            if self.checkGood(i):
                c+=1
        return c

s=Solution()
print(s.rotatedDigits(10000))