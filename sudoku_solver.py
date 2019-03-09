from pprint import pprint
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def get_choices(b, x, y):
            ans = {str(i) for i in range(1, 10)}
            for i in range(0, 9):
                if b[x][i] in ans:
                    ans.remove(b[x][i])
                if b[i][y] in ans:
                    ans.remove(b[i][y])
            xb,yb = x//3, y//3
            for i in range(3):
                for j in range(3):
                    if b[xb*3 + i][yb*3 + j] in ans:
                        ans.remove(b[xb*3+i][yb*3+j])
            return ans

        def build(b):
            next_pos = False
            i=0
            while i<9:
                j=0
                while j<9:
                  if b[i][j] == ".":
                      next_pos = True
                      break
                  j+=1
                if next_pos:
                    break
                i+=1


            if not next_pos:
                return True

            choices = get_choices(b, i, j)
            for c in choices:
                b[i][j] = c
                result = build(b)
                if result:
                    return True
            b[i][j] = "."
            return False
        build(board)

s = Solution()
inp = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s.solveSudoku(inp)
pprint(inp)