class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l==0:
            return 0
        if s==s[::-1]:
            return 0
        pal = [[0]*l for _ in range(l)]
        for i in range(l):
            pal[i][i] = 1
        for i in range(l-1):
            if s[i] == s[i+1]:
                pal[i][i+1] = 1
        
        k=2
        while k<l:
            for i in range(l-k):
                j = i+k
                if s[i] == s[j]:
                    pal[i][j] = pal[i+1][j-1]
            k+=1

        opt = [float("inf")]*(1+l)
        opt[0] = 0
        opt[1] = 1
        for i in range(2, l+1):
            for j in range(i):
                if pal[j][i-1] == 1:
                    opt[i] = min(opt[i], opt[j]+1)
        return opt[l]

print(Solution().minCut("abbadeed"))