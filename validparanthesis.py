class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        ans = 0
        i = 0
        l = len(s)
        count = 0
        while i<l:
            if len(stack) == 0:
                if s[i] == "(":
                    stack.append(s[i])
                i+=1
            else:
                cur = stack[-1]
                print(stack, count, s[i], cur)
                if s[i] == ")" and cur == "(":
                    stack.pop()
                    count += 2
                elif s[i] == "(":
                    stack.append(s[i])
                i+=1
            if count > ans:
                ans = count
        return ans
s=Solution()
print(s.longestValidParentheses(""))