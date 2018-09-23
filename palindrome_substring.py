class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(s, l, r, n):
            while l>=0 and r<n and s[l] == s[r]:
                l-=1
                r+=1
            return r-l-1, s[l+1:r]

        def develop(s, i, n):
            oddl, odda = expand(s, i, i, n)
            evenl, evena = expand(s, i-1, i, n)
            if oddl < evenl:
                return evenl, evena
            return oddl, odda

        ans = ""
        ansl = 0
        n = len(s)
        for i in range(n):
            curl, cur = develop(s, i, n)
            if ansl < curl:
                ansl = curl
                ans = cur
        return ans

s = Solution()
print(s.longestPalindrome(""))

