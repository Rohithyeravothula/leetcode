class Solution:
    def letterCasePermutation(self, s):
        """
        :type S: str
        :rtype: List[str]
        """
        if not s:
            return [s]
        def get(s, c, l):
            # print(c, l)
            if c>=l:
                return []
            i = c+1
            while i<l:
                if s[i].isalpha():
                    break
                i+=1
            if i>=l:
                if s[c].isalpha():
                    return [s[:c] + s[c].upper() + s[c+1:], s[:c] + s[c].lower() + s[c+1:]]
                else:
                    return [s[:]]
            cur = get(s, i, l)
            if not s[c].isalpha():
                return cur
            ans = []
            for p in cur:
                ans.append(p[:c] + p[c].upper() + p[c+1:])
                ans.append(p[:c] + p[c].lower() + p[c+1:])
            return ans
        return get(s, 0, len(s)) 

s = Solution()
inp = "a1B2"
print(s.letterCasePermutation(inp))