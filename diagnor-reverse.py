class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        traversal = True
        incr = True
        l = len(matrix)
        b = len(matrix[0])
        ans = []
        for i in range(0, b):
            u = 0 
            v = i
            cur = []
            while (u<l and v>=0):
                cur.append(matrix[u][v])
                u+=1
                v-=1
            if traversal:
                cur = cur[::-1]
            ans += cur
            traversal = not traversal
            # print(ans, cur)
        for i in range(1, l):
            u = i
            v = b-1
            cur = []
            while (u<l and v>=0):
                cur.append(matrix[u][v])
                u += 1
                v -= 1
            if traversal:
                cur = cur[::-1]
            ans += cur
            traversal = not traversal
        return ans

m=[ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ], [10, 11, 12]]
s=Solution()
s.findDiagonalOrder(m)
