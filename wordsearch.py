class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        pos = []
        l = len(board)
        b = len(board[0])
        wl = len(word)
        if wl == 0:
            return False
        for i in range(0, l):
            for j in range(0, b):
                if board[i][j] == word[0]:
                    pos.append([i, j])

        def check_path(visited, i, j, wi, wl):
            if i>=0 and i<l and j>=0 and j<b and visited[i][j] == 0 and board[i][j] == word[wi]:
                if wi == wl-1:
                    return True
                elif wi<wl-1:
                    visited[i][j] = 1
                    ans = check_path(visited, i+1, j, wi+1, wl) or check_path(visited, i-1, j, wi+1, wl) or check_path(visited, i, j+1, wi+1, wl) or check_path(visited, i, j-1, wi+1, wl)
                    visited[i][j] = 0
                    return ans
            return False

        v = []
        for i in range(0, l):
            v.append([0]*b)
        for p in pos:
            if check_path(v, p[0], p[1], 0, wl):
                return True
        return False

    def findWords(self, board, words):
        words = list(set(words))
        ans = []
        for w in words:
            if self.exist(board, w):
                ans.append(w)
        return ans




bd = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
st = "A"
s=Solution()
print(s.exist(bd, st))