class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # print(s)
        l = len(s)
        i = 0
        j = l-1
        while i<j:
            # print(s[i:j+1])
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower()!=s[j].lower():
                    return False
                else:
                    i+=1
                    j-=1
            while i<l and not s[i].isalnum():
                i+=1
            while j>=0 and not s[j].isalnum():
                j-=1
        return True

        
s=Solution()
print(s.isPalindrome(" a "))