class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        stk = []
        i = 0
        l = len(s)
        count = 0
        while i<l:
            if s[i] == "(":
                stk.append(s[i])
            elif s[i] == ")":
                if stk:
                    count+=2
                    stk.pop()
                    if not stk:
                        ans = max(ans, count)
                else:
                    ans = max(ans, count)
                    count = 0
            i+=1
        if not stk:
            return max(ans, count)
        return ans

s=Solution()
print(s.longestValidParentheses("((()"))