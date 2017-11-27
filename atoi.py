import math
class Solution:
    def toInt(self, s):
        ans = 0
        for i in s:
            o = ord(i)
            if o<ord('9') and o>ord('0'):
                ans = ans*10 + o-ord('0')
            else:
                return None, False
        return ans, True

    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        neg = 1
        if s[0] == '-':
            neg = -1
            s=s[1:]
        elif s[0] == '+':
            s=s[1:]
        if 'e' in s:
            n,p = s.split('e')
            n, ch = self.toInt(n)
            if ch is False:
                return 0
            p, ch = self.toInt(p)
            if ch is False:
                return 0
            ans = n * int(math.pow(10, p))
        else:
            ans, ch = self.toInt(s)
            if ch is False:
                return 0
        return ans*neg


s=Solution()
# print(s.toInt(""))
# print(s.toInt("1"))
# print(s.toInt("-1"))
# print(s.toInt("-0"))
# print(s.toInt("+0"))
# print(s.toInt("321"))
# print(s.toInt("-123"))
# print(s.toInt("23e4"))
# print(s.toInt("-32e2"))
print(s.myAtoi(""))
print(s.myAtoi("1"))
print(s.myAtoi("-1"))
print(s.myAtoi("-0"))
print(s.myAtoi("+0"))
print(s.myAtoi("321"))
print(s.myAtoi("-123"))
print(s.myAtoi("23e4"))
print(s.myAtoi("-32e2"))
print(s.myAtoi("-as34"))