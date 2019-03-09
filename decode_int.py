class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if "00" in s or not s or s[0] == '0':
            return 0
        l = len(s)
        A = ord('A')-1
        first = None
        second = 1
        i=1
        valid_range = range(1, 27)
        while i<l:
            cur_decode = 0
            if s[i] != '0':
                cur = chr(A+int(s[i]))
                cur_decode += second
                if s[i-1] != '0' and int(s[i-1:i+1]) in valid_range:
                    if first is None:
                        first = 1
                    cur_decode += first
            elif int(s[i-1:i+1]) in valid_range:
                cur = chr(A+int(s[i-1:i+1]))
                if first is None:
                    first = 1
                cur_decode += first

            # print(cur_decode)

            first = second
            second = cur_decode
            i+=1
        return second

# 12412031023130021034
print(Solution().numDecodings(""))