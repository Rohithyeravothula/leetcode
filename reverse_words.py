class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        def reverse(cur, s, e):
            i,j = s,e
            while i<j:
                cur[i], cur[j] = cur[j], cur[i]
                i+=1
                j-=1
        s = list(s)
        prev = 0
        l = len(s)
        i = 0
        while i<l and s[i] == " ":
            i+=1
        if i==l:
            return ""
        while i<l:
            while i<l and s[i] != " ":
                s[prev] = s[i]
                i+=1
                prev += 1
            if i<l:
                s[prev] = s[i]
                prev += 1
                i+=1
            while i<l and s[i] == " ":
                i+=1
        if s[prev-1] == " ":
            prev -= 1

        s = s[:prev]
        # print(s)
        l = len(s)
        prev = 0
        i = 0
        while i<l:
            while i< l and s[i]!=" ":
                i+=1
            reverse(s, prev, i-1)
            i+=1
            prev = i
        reverse(s, 0, l-1)
        return "".join(s)

inp = "the sky is    blue        "
inp = "  a  he this a mad "
inp = "    "
s = Solution().reverseWords(inp)
print(s, len(s))