import math
class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        ans = "0."
        if numerator >= denominator:
            ans = str(numerator/denominator) + "."
            numerator = numerator % denominator
        visited = {}
        recurring = False
        r_start = 0
        index = 0
        while numerator != 0:
            count = 1
            # print(numerator, denominator, ans)
            while numerator < denominator:
                numerator = numerator*10
                count *= 10
            cur = int(numerator/denominator)
            numerator = numerator % denominator
            if numerator in visited:
                recurring = True
                r_start = visited[numerator]
                break
            # print(count)
            visited[numerator] = index
            index += 1
            ans = ans + str(cur*count)[::-1]
            numerator = numerator*10
            count = count*10
            print(numerator, visited, ans)
        deci = ans.split(".")[1]

        if float(int(ans)) == ans:
            return str(int(ans))
        if recurring:
            cur = str(ans).split(".")
            prev = cur[0]
            deci = cur[1][:r_start]
            recur = "(" + cur[1][r_start:] + ")"
            return prev + "." + deci + recur
        return str(ans)

s=Solution()
print(s.fractionToDecimal(1,2))