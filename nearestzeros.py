class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        l = len(matrix)
        if l==0:
            return matrix
        b = len(matrix[0])
        dist = [[float("inf")] * b for _ in range(0, l)]
        for i in range(0, l):
            for j in range(0, b):
                if matrix[i][j] == 0:
                    dist[i][j] = 0


        # top down
        for i in range(1, l):
            dist[i][0] = min(dist[i][0], 1+dist[i-1][0])

        for i in range(1, b):
            dist[0][i] = min(dist[0][i], 1+dist[0][i-1])

        for i in range(1, l):
            for j in range(1, b):
                dist[i][j] = min(dist[i][j], 1+min(dist[i-1][j], dist[i][j-1])) 

        # bottem iteration
        for i in range(l-2, -1, -1):
            dist[i][b-1] = min(dist[i][b-1], 1+dist[i+1][b-1])

        for i in range(b-2, -1, -1):
            dist[l-1][i] = min(dist[l-1][i], 1+dist[l-1][i+1])

        for i in range(l-2, -1, -1):
            for j in range(b-2, -1, -1):
                dist[i][j] = min(dist[i][j], 1+min(dist[i+1][j], dist[i][j+1]))

        for i in range(0, l):
            for j in range(0, b):
                if dist[i][j] == float("inf"):
                    dist[i][j] = -1

        return dist

m=[[0,0,0],[0,1,0],[0,0,0]]
s=Solution()
print(s.updateMatrix(m))