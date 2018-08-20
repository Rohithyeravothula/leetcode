class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if not A or not B:
            return []
        la = len(A)
        lb = len(B)
        opt = [[0]*(lb+1) for _ in range(la+1)]
        for i in range(1, la+1):
            for j in range(1, lb+1):
                if A[i-1] == B[j-1]:
                    opt[i][j] = 1+opt[i-1][j-1]

        return max([max(row) for row in opt])

    def get_common_array(self, opt, A):
        max_l = max([max(row) for row in opt])
        if max_l == 0:
            return []
        for i in range(la+1):
            for j in range(lb+1):
                if opt[i][j] == max_l:
                    return A[i - max_l: i+1]

a = [1, 0]
b = [2,3,1,2,3,1,2]
s = Solution()
print(s.findLength(a, b))
