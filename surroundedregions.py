from extras import *


from collections import deque
class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def get_O_children(board, pos, l, b):
            children = []
            x = pos[0]
            y = pos[1]
            print(x,y,l,b)
            if x+1<l and board[x+1][y] == "O":
                children.append([x+1, y])
            if y+1<b and board[x][y+1] == "O":
                children.append([x, y+1])
            if x-1>0 and board[x-1][y] == "O":
                children.append([x-1, y])
            if y-1>0 and board[x][y-1] == "O":
                children.append([x, y-1])
            return children

        l = len(board)
        if l == 0:
            return None
        if l>=3:
            b = len(board[0])
            border = []
            for i in range(0, l):
                if board[i][0] == "O":
                    border.append([i, 0])
                if board[i][b-1] == "O":
                    border.append([i, b-1])

            for j in range(0, b):
                if board[0][j] == "O":
                    border.append([0, j])
                if board[l-1][j] == "O":
                    border.append([l-1, j])

            # print(border)
            for pos in border:
                board[pos[0]][pos[1]] = "P"

            queue = deque(border)
            while len(queue) != 0:
                cur = queue.popleft()
                children = get_O_children(board, cur, l, b)
                for c in children:
                    board[c[0]][c[1]] = "P"
                queue.extend(children)

            # print_2d_array(board)
            for i in range(0, l):
                for j in range(0, b):
                    if board[i][j] == "O":
                        board[i][j] = "X"

            for i in range(0, l):
                for j in range(0, b):
                    if board[i][j] == "P":
                        board[i][j] = "O"


inp = [["X","X","O","X"], ["X","X","O","X"], ["X","X","O","X"]]
s=Solution()
# print_2d_array(inp)
s.solve(inp)
print_2d_array(inp)