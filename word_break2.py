class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        l = len(s)
        wordDict = set(wordDict)
        opt = [0]*(1+l)
        opt[0] = 1
        for i in range(1, l+1):
            for j in range(i):
                if opt[j] == 1 and (s[j:i] in wordDict):
                    opt[i] = 1
        def recover(a, index):
            sol = []
            if s[:index] in wordDict:
                sol.append(s[:index])
            for i in range(1, index):
                if a[i] == 1 and (s[i:index] in wordDict):
                    cur = [word+" " + s[i:index] for word in recover(a, i)]
                    sol.extend(cur)
            return sol

        if opt[l] == 0:
            return []
        return recover(opt, l)



w = "pineapplepenapplea"
wd = ["apple", "pen", "applepen", "pine", "pineapple"]
s = Solution()
print(s.wordBreak(w, wd))