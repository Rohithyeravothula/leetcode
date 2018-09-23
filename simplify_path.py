class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = [s for s in path.split("/") if s and s!="."]
        l = len(path)
        stk = []
        i = 0
        while i < l:
            if path[i] == "..":
                if stk:
                    stk.pop()
            else:
                stk.append(path[i])
            i+=1
        ans = "/".join(stk)
        return "/" + ans

s = Solution()
print(s.simplifyPath("/./b"))
