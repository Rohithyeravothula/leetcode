class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        def extend_palindrome(left, right):
            count = 0
            while left >= 0 and right < l and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count

        ans = 0
        for i in range(l):
            ans += extend_palindrome(i, i)
            ans += extend_palindrome(i, i+1)
        return ans


s = Solution()
print(s.countSubstrings("aaaa"))
