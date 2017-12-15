class Solution(object):
    def searchMatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: bool
        """
        l=len(matrix)
        if l==0:
            return False
        b=len(matrix[0])
        i = l-1
        j = 0
        while i>=0 and j<b:
            if matrix[i][j] == k:
                return True
            elif matrix[i][j] > k:
                i-=1
            elif matrix[i][j] < k:
                j+=1
        return False