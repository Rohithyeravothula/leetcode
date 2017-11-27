
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def ch(n):
            digits = list(str(n))
            l=len(digits)
            for i in range(0, l):
                digits[i] = int(digits[i])
            for d in digits:
                if d==0:
                    return False
                elif n%d!=0:
                    return False
            return True


        ans = []
        for i in range(left, right+1):
            if ch(i):
                ans.append(i)
        return ans


s=Solution()
print(s.selfDividingNumbers(1, 22))
# for d in digits:
#   if d==2 and digits[-1] %2 != 0:
#       return False
#   elif d==3 and s % 2 != 0: