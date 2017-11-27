class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l == 0 or s[0] == '0':
            return 0
        elif l == 1:
            return 1

        a = [0]*(l+1)
        a[l] = 1
        if s[l-1] != '0':
            a[l-1] = 1

        for i in range(l-2, -1, -1):
            if s[i] != '0':
                if int(s[i:i+2]) <= 26:
                    a[i] = a[i+1] + a[i+2]
                else:
                    a[i] = a[i+1]
        return a[0]
        
s=Solution()
# for i in range(1, 35):
#     print(i, s.numDecodings(str(i)))
print(s.numDecodings("24"))