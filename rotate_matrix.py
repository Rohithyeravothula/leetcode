class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        for i in range(l):
        	for j in range(i):
        		matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(l):
        	for j in range(l//2):
        		matrix[i][j], matrix[i][l-j-1] = matrix[i][l-j-1], matrix[i][j]