class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def match(s1,i, s2,j):
            if j == len(s2):
                return i,j

            if s2[j] == "*":
                return match(s1,i, s2,j+1)

            if i == len(s1):
                return None

            if s1[i] != s2[j]:
                return match(s1, i+1, s2, j)

            if s1[i] == s2[j] or s2[j] == "?":
                return match(s1,i+1, s2,j+1)




        i = 0
        j = 0
        sl = len(s)
        pl = len(p)
        while i<sl and j<pl:
            if s[i] == p[j] or p[j] == "?":
                i+=1
                j+=1
            elif p[j] == "*":
                m = match(s,i,p,j)
                if not m:
                    return False
                i,j = m
            elif s[i] != p[j]:
                return False
        if (i==sl and j==pl) or (j==pl and j>0 and p[j-1] == "*"):
            return True
        return False



s1 = ""
s2 = "a"
print(Solution().isMatch(s1, s2))

