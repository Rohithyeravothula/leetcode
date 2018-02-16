class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        row = 0
        col = 0
        while row < m and col < n:
        	i=row
        	j=col
        	num = matrix[i][j]
        	while i<m and j<n:
        		if num!=matrix[i][j]:
        			return False
        		j+=1
        		i+=1
        	col+=1

        row = 1
        col = 0
        while row<m and col<n:
        	i=row
        	j=col
        	num = matrix[i][j]
        	while i<m and j<n:
        		if num!=matrix[i][j]:
        			return False
        		i+=1
        		j+=1
        	row+=1
        return True


mtr=[[1,2,4,5,3],[4,12,3,4,2,3]]
s=Solution()
print(s.isToeplitzMatrix(mtr))
