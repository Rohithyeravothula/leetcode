class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        opt = [[0] * (l+1) for _ in range(0, l+1)]
        row = 0
        col = 1
        for i in range(1, l):
            if s[i-1:i+1] == "()":
                opt[i][i+1] = 2
        # for i in opt:
        #     print(i)
        while row <= l and col <= l:
            i = row
            j = col
            while i<=l and j<=l:
                for k in range(i, j):
                    opt[i][j] = max(opt[i][j], opt[i][k]+opt[k+1][j])
                i+=1
                j+=1
            col+=1 
        for i in opt:
            print(i)
s=Solution()
print(s.longestValidParentheses("((()))"))