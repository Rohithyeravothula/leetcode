class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        l = len(A)
        b = len(B)
        if l==0 or b==0:
            return 0

        opt = [0]*b
        for i in range(0, b):
            if A[0] == B[i]:
                opt[i] = 1
        maxl = max(opt)
        for i in range(1, l):
            # print(opt)
            for j in range(b-1, 0, -1):
                if A[i] == B[j]:
                    opt[j] = 1+opt[j-1]
                else:
                    opt[j] = 0
            if A[i] == B[0]:
                opt[0] = 1
            else:
                opt[0] = 0
            maxl = max(maxl, max(opt))
        # print(opt)
        return maxl

a=[1,2,3,2,1]
b=[3,2,1,4,7]
s=Solution()
print(s.findLength(a,b))