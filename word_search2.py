class Trie:
    def __init__(self):
        self.data = {}

    def insert(self, word):
        def _insert(word, i, l, data):
            if word[i] not in data: data[word[i]] = {}
            if i==l-1:
                data[word[i]]['leaf'] = word
            else:
                _insert(word, i+1, l, data[word[i]])
        if word:
            _insert(word, 0, len(word), self.data)



class Solution:
    def findWords(self, board: 'List[List[str]]', words: 'List[str]') -> 'List[str]':
        if not board:
            return []
        t = Trie()
        for word in words:
            t.insert(word)
        found = set()

        def get_children(i,j,l,b):
            ans = [(i,j+1), (i, j-1), (i+1, j), (i-1, j)]
            return [(x,y) for x,y in ans if (x>=0 and x<l) and (y>=0 and y<b)]


        def dfs(i, j, pe, found, data, l, b):
            char = board[i][j]
            
            pe.add((i,j))
            if char in data:
                if "leaf" in data[char]:
                    found.add(data[char]["leaf"])
                for (x,y) in get_children(i,j,l,b):
                    if (x,y) not in pe:
                        dfs(x,y,pe,found,data[char],l,b)
            pe.remove((i,j))

        found = set()
        l = len(board)
        b = len(board[0])
        wl = len(words)
        for i in range(l):
            for j in range(b):
                if board[i][j] in t.data:
                    dfs(i,j,set(),found, t.data,l,b)
                if len(found) == wl:
                    return words
        return list(found)

# words = ["oath","pea","eat","rain"]
# board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ['rambo']
board = [['r'], ['a'], ['m'], ['b'], ['o']]
board = [["a","b"],["a","a"]]
words = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]
print(Solution().findWords(board, words))

# t = Trie()
# for w in words:
#     t.insert(w)
# print(t.data)

"""
t.insert("hello")
t.insert("hell")
t.insert("abb")
"""