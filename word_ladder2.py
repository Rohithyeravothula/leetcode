import string
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if beginWord == endWord:
            return 0
        l = len(beginWord)
        seen = {beginWord}
        cur = [beginWord]
        wordList = set(wordList)
        if not wordList or endWord not in wordList:
            return 0
        steps = 1
        while cur:
            steps += 1
            newcur = []
            for s in cur:
                for i in range(l):
                    for char in string.ascii_lowercase:
                        sp = s[:i] + char + s[i+1:]
                        if sp == endWord:
                            return steps
                        elif sp not in seen and sp in wordList:
                            newcur.append(sp)
                            seen.add(sp)
                seen.add(s)
            cur = newcur
        return 0

    def findLadders(self, beginWord, endWord, wordList):
        self.min_length = self.ladderLength(beginWord, endWord, wordList)
        self.sol = []
        l = len(beginWord)

        def dfs(cur, path):
            pl = len(path)
            if pl > self.min_length:
                return

            if cur == endWord and pl == self.min_length:
                self.sol.append(path)
                return 

            sol = []
            for i in range(l):
                for char in string.ascii_lowercase:
                    nw = cur[:i] + char + cur[i+1:]
                    if nw != cur and nw in wordList and nw not in path:
                        dfs(nw, path + [nw])

        dfs(beginWord, [beginWord])
        return self.sol



bw,ew,wl = "hit", "cog", ["hot","dot","dog","lot","log","cog"]
bw,ew,wl = "hit", "cod", ['hot', 'cot', 'cod']
print(Solution().findLadders(bw, ew, wl))


