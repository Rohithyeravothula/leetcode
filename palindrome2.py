class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s==s[::-1]:
            return True
        l=len(s)
        i=0
        j=l-1
        while i<j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                p1 = s[i:j]
                p2 = s[i+1:j+1]
                if p1 == p1[::-1] or p2 == p2[::-1]:
                    return True
                return False
        return True

s = Solution()
print(s.validPalindrome(""))