class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l==0:
            return 0
        prev = [0]*l
        prev[0] = 1
        for i in range(1, l):
            a=[0]*l
            a[i]=1
            for j in range(i-1, -1, -1):
                if s[i] == s[j]:
                    a[j] = 2+prev[j+1]
                else:
                    a[j] = max(a[j+1], prev[j])
            # print(prev, a)
            prev = a
        return prev[0]

s=Solution()
print(s.longestPalindromeSubseq("malayalam"))



