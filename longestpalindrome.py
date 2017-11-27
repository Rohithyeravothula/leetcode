
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l == 0:
            return 0
        opt = [[0] * l for _ in range(0, l)]
        for i in range(0, l):
            opt[i][i] = 1
        for i in range(1, l):
            if s[i] == s[i-1]:
                opt[i-1][i] = 2

        row = 0
        col = 2
        while row < l and col < l:
            i = row
            j = col
            while i<l and j<l:
                if s[i] == s[j] and opt[i+1][j-1] != 0:
                    opt[i][j] = 2+opt[i+1][j-1]
                i+=1
                j+=1
            col+=1
        # printMatrix(opt)
        m = 1
        ms = 0
        me = 0
        for i in range(0, l):
            for j in range(0, l):
                if opt[i][j] > m:
                    m = opt[i][j]
                    ms = i
                    me = j 
        return s[ms:me+1]

s=Solution()
print(s.longestPalindrome(""))