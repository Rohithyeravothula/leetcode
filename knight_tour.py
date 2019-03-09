def say_hello():
    print('Hello, World')

for i in range(5):
    say_hello()


# 
# Your previous Plain Text content is preserved below:
# 
# Welcome to your interviewing.io interview.
# 
# Once you and your partner have joined, a voice call will start automatically.
# 
# Use the language dropdown near the top right to select the language you would like to use.
# 
# You can run code by hitting the 'Run' button near the top left.
# 
# Enjoy your interview!
# 
# 
# 
# 
# The game of chess is played on a square grid of size 8x8. There is a chess-piece
# called a knight that moves by jumping in an L-shape: 2 steps in x and 1 step
# in y or 1 step in x and 2 steps in y. 
# 
# For example, a possible move from (3,3) would be to (5,4). When moving from
# (3,3) to (5,4), the knight doesn't touch the intervening squares.
# 
# 
# 1. Write a function that enumerates the valid moves from a starting position
# (5,2),(5,4),(...
# 
#  (x,y) => (1,2) (2,1) +,1
#            (-1,2), (1, -2), (-1,-2)...
# 
# 
# -- 
# 2.
# A knight's tour is a sequence of legal moves for a knight on an otherwise empty chessboard subject to two constraints:
#  - The knight ends up on the same square it started from
#  - The knight touches every other square on the board once
# 
# 2. Given a board size N, return a valid knight's tour if one exists for that
#  board.
# 
# 
# 



def get_moves(x,y,n):
    numbers = [1,2]
    signs = [-1,1]
    moves = []
    for xn in numbers:
        for yn in numbers:
            if xn == yn:
                continue
            for xs in signs:
                for ys in signs:
                    xnew = x + xs*xn
                    ynew = y + ys*yn
                    moves.append((xnew, ynew))
    
    valid_moves = []
    valid_range = range(0, n)
    for xn, yn in moves:
        if xn in valid_range and yn in valid_range:
            valid_moves.append((xn, yn))
    return valid_moves
                    
# print(get_moves(0,0,4))
# print(get_moves(3,3))



# use a DFS searching mechanism
# Keep a list of visited squares
# make sure if I hit start position check if I have visited all nodes
# keep the path I have traversed so far

def dfs(x,y,seen,path,n):
    children = get_moves(x,y,n)
    for child in children:
        if child not in seen:
            seen.add(child)
            curpath = dfs(child[0], child[1], seen, path+[child],n)
            if curpath:
                return curpath
            seen.remove(child)
    # print(path, seen)
    if len(path) == n*n and (0,0) in children:
        return path
    return None

def get_knights_tour(n):
    seen = {(0,0)}
    ipath = [(0,0)]
    tour = dfs(0,0,seen, ipath,n)
    return tour if tour else []
        
            
print(get_knights_tour(6))








