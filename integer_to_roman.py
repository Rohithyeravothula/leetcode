class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        m = ["", "M", "MM", "MMM"]
        c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return str(m[(num%10000)//1000]) + str(c[(num%1000)//100]) + str(x[(num%100)//10]) + str(i[(num%10)])

s = Solution()
print(s.intToRoman(98))



            