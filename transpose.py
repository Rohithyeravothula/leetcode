class Solution:
    def transpose(self, a):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if not a:
            return a
        l = len(a)
        b = len(a[0])
        tp = [[0]*l for _ in range(b)]
        for i in range(b):
            for j in range(l):
                tp[i][j] = a[j][i]
        return tp
s = Solution()
# inp = [[1,2,3],[4,5,6],[7,8,9]]
# inp = [[1,2,3],[4,5,6]]
# inp = [[1,2,3,4]]
inp = []
print(s.transpose(inp))