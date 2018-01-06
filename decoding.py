class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk = []
        i = 0
        l = len(s)
        ans = ""
        while i<l:
            if s[i] == "]":
                cur = ""
                while True:
                    left = stk.pop()
                    if left=="[":
                        break
                    cur = cur+left[::-1]
                cur = cur[::-1]
                n = ""
                while stk:
                    left = stk.pop()
                    if left.isdigit():
                        n+=left                     
                    else:
                        stk.append(left)
                        break
                print(cur, n)
                n=int(n[::-1])
                stk.append(cur*n)
                print(stk)
            else:
                stk.append(s[i])
            i+=1
        return "".join(stk)
s=Solution()
print(s.decodeString("2[ab3[cd]]4[xy]"))