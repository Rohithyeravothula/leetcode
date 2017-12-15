class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = 2*n
        stack = ["()"]
        ans = []
        while len(stack) != 0:
            # print(stack)
            cur = stack.pop()
            cur_l = len(cur)
            if cur_l < l:
                children = []
                for i in range(0, int(cur_l/2)):
                    children.append(cur[0:i] + "()" + cur[i:])
                    children.append(cur[0:i] + "(" + cur[i:cur_l-i] + ")" + cur[cur_l-i:])
                    # print(i, cur, children)
                stack.extend(list(set(children)))
            elif cur_l == l:
                ans.append(cur)
        return list(set(ans))

s=Solution()
print(s.generateParenthesis(0))