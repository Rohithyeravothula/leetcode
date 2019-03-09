class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sl = len(s)
        pl = len(p)
        opt = [[False]*(1+pl) for _ in range((1+sl))]
        opt[0][0] = True

        # if . found break, after that string cannot be reduced to null
        for j in range(1, 1+pl):
            if p[j-1] == "*":
                opt[0][j] = opt[0][j-2]

        for i in range(1, 1+sl):
            for j in range(1, 1+pl):
                if s[i-1] == p[j-1] or p[j-1] == ".":
                    opt[i][j] = opt[i-1][j-1]
                elif p[j-1] == "*":
                    opt[i][j] = opt[i][j-2]
                    first_match = (p[j-2] == "." or p[j-2] == s[i-1])
                    opt[i][j] = opt[i][j] or (first_match and opt[i-1][j])

        # for row in opt:
        #     print(row)
        return opt[sl][pl]


s1 = "abeffe"
s2 = "ab.*e"
print(Solution().isMatch(s1, s2))

    

