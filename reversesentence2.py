class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        inp = s.split()
        return " ".join(inp[::-1])




s=Solution()
inp = "   a   b "  
ans = s.reverseWords(inp)
print(ans)