from collections import Counter
class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """        
        s = set(S)
        t = Counter(T)
        ans = []
        for c in S:
            ans.append(c*t[c])
        for c in t.keys():
            if c not in s:
                ans.append(c*t[c])
        return "".join(ans)


s = Solution()
print(s.customSortString("czbamk", "zaddbc"))
