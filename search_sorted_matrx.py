class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or matrix == [[]]:
            return False
        l = len(matrix)
        b = len(matrix[0])

        if matrix[0][0] > target or matrix[l-1][b-1] < target:
            return False

        left, right = 0, l-1
        while left <= right:
            mid = (left + right) >> 1
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        left -= 1

        start, end = 0, b-1
        while start <= end:
            mid = (start + end) >> 1
            if matrix[left][mid] == target:
                return True
            elif matrix[left][mid] < target:
                start = mid+1
            else:
                end = mid-1
        return False


inp = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
print(Solution().searchMatrix(inp, 24))