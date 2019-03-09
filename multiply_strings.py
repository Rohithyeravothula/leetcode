class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def strip(num):
            l = len(num)
            i = 0
            while i<l and num[i] == 0:
                i+=1
            return num[i:] if num[i:] else [0]

        def add(s1, s2):
            s1 = s1[::-1]
            s2 = s2[::-1]
            l1, l2 = len(s1), len(s2)
            i,j = 0,0
            ans = []
            c = 0
            while i<l1 or j<l2 or c:
                d1 = s1[i] if i<l1 else 0
                d2 = s2[j] if j<l2 else 0
                cursum = d1 + d2 + c
                ans.append(cursum%10)
                c = cursum//10
                i+=1
                j+=1
            return ans[::-1]

        def mul(num, d):
            num = num[::-1]
            ans = []
            c = 0
            for val in num:
                cursum = c + val*d
                ans.append(cursum%10)
                c = cursum//10
            if c>0:
                ans.append(c)
            return ans[::-1]

        num1 = strip([int(val) for val in list(num1)])
        num2 = strip([int(val) for val in list(num2)])
        ans = [0]
        c = 0
        for d in num2[::-1]:
            cursum = mul(num1, d)
            ans = add(ans, cursum+[0]*c)
            c+=1
        return "".join(str(val) for val in strip(ans))

print(Solution().multiply("0009", "1"))


