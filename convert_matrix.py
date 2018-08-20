class Solution:

    def update_to(self, matrix, row, column, number, l, b):
        for i in range(l):
            if matrix[i][column] != 0:
                matrix[i][column] = number
        for j in range(b):
            if matrix[row][j] != 0:
                matrix[row][j] = number

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        place_holder = float("inf")
        if not matrix:
            return
        l = len(matrix)
        b = len(matrix[0])
        for i in range(l):
            for j in range(b):
                if matrix[i][j] == 0:
                    self.update_to(matrix, i, j, place_holder, l, b)

        for i in range(l):
            for j in range(b):
                if matrix[i][j] == place_holder:
                    matrix[i][j] = 0

mx = [[1,1,1,1], [0,1,1,1]]
s = Solution()
s.setZeroes(mx)
print(mx)
