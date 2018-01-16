class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stk = []
        score_stk = [0]
        i = 0
        l = len(s)
        cur_score = 0
        while i<l:
            print(stk, score_stk)
            if len(stk) == 0:
                if s[i] == "(":
                    stk.append(s[i])
                elif s[i] == ")":
                    cur_score = 0
                    score_stk.append(cur_score)
            else:
                if s[i] == "(":
                    stk.append(s[i])
                elif s[i] == ")":
                    if stk[-1] == "(":
                        cur_score = score_stk.pop()
                        cur_score+=2
                        stk.pop()
                        score_stk.append(cur_score)
            i+=1
        return max(score_stk)
s=Solution()
print(s.longestValidParentheses("()(()"))
# ()()))((()))()()
# ()()))(())
