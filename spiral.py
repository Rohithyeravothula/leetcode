class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def spiral(a, row_start, row_end, col_start, col_end, result):
            m = row_end - row_start
            n = col_end - col_start
            if m==0 or n==0:
                return result
            elif m==1:
                for i in range(col_start, col_end):
                    result.append(a[row_start][i])
                return result
            elif n==1:
                for i in range(row_start, row_end):
                    result.append(a[i][col_start])
                return result
            else:
                for i in range(col_start, col_end):
                    result.append(a[row_start][i])

                for i in range(row_start + 1, row_end):
                    result.append(a[i][col_end-1])

                for i in range(col_end-2, col_start-1, -1):
                    result.append(a[row_end-1][i])

                for i in range(row_end-2, row_start, -1):
                    result.append(a[i][col_start])
                return spiral(a, row_start+1, row_end-1, col_start+1, col_end-1, result)
        ans = []
        l = len(matrix)
        if l == 0:
            return ans
        b = len(matrix[0])
        spiral(matrix, 0, l, 0, b, ans)
        return ans


test = [[1], [2], [3]]
s=Solution()
print(s.spiralOrder(test))