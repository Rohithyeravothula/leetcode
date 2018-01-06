class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = ""
        if numerator*denominator < 0:
            sign = "-"
            numerator = abs(numerator)
            denominator = abs(denominator)
        non_decimal = sign + str(numerator//denominator)
        ans = ""
        numerator = (numerator % denominator)
        remainders = {numerator:0}
        while numerator != 0:
            numerator*=10
            ans += str(numerator//denominator)
            numerator = numerator%denominator
            if numerator in remainders:
                index = remainders[numerator]
                ans = ans[0:index] + "(" + ans[index:]+")"
                break
            else:
                remainders[numerator] = len(ans)

        if ans == "":
            return non_decimal
        return "{}.{}".format(non_decimal, ans)



s=Solution()
print(s.fractionToDecimal(-50, -8))
# for i in range(1,20):
#     print("1/{}".format(i), s.fractionToDecimal(1,i))