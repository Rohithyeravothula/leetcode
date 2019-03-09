class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = set()
        l = len(board)
        for i in range(l):
            for j in range(l):
                if board[i][j] != ".":
                    bi = int(board[i][j])
                    if bi < 1 or bi > 9:
                        return False
                    row_key = "r{}{}".format(i, board[i][j])
                    if row_key in seen:
                        return False
                    col_key = "c{}{}".format(j, board[i][j])
                    if col_key in seen:
                        return False
                    block_key = "r{}c{}{}".format(i//3, j//3, board[i][j])
                    if block_key in seen:
                        return False
                    seen.add(row_key)
                    seen.add(col_key)
                    seen.add(block_key)
        return True
