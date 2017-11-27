class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if s == "":
            return False
        d = {}
        for i in wordDict:
            d[i] = 1
        l = len(s)
        a=[0]*(l+1)
        # print(l, a, s)
        a[0] = 1
        for i in range(1, l+1):
            for j in range(0, i):
                if a[j] == 1 and s[j:i] in d:
                    a[i] = 1
                    break
        # print(a)
        if a[l] == 1:
            return True
        return False

st = ""
wd = ["cat", "cats", "leet", "code"]
s=Solution()
print(s.wordBreak(st,wd))
