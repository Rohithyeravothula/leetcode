class Solution:
    def add(self, num1, num2):
        num1 = num1[::-1]
        num2 = num2[::-1]
        ans = ""
        num1_length = len(num1)
        num2_length = len(num2)
        i = 0
        j = 0
        carry = 0
        while i<num1_length and j<num2_length:
            digit = int(num1[i]) + int(num2[j]) + carry
            carry = digit//10
            digit = digit%10
            ans += str(digit)
            i+=1
            j+=1


        while i<num1_length:
            digit = int(num1[i]) + carry
            carry = digit//10
            digit = digit%10
            ans += str(digit)
            i+=1


        while j<num2_length:
            digit = int(num2[j]) + carry
            carry = digit//10
            digit = digit%10
            ans += str(digit)
            j+=1

        # print(ans, carry)
        if carry:
            ans += str(carry)

        ans = ans[::-1]
        i=0
        l = len(ans)
        while i<l and ans[i] == "0":
            i+=1    
        print("adding ", num1, num2)    
        print("returning: ", ans[i:])
        return a[i:]

    def multiply_digit(self, nums, digit):
        nums = nums[::-1]
        digit = int(digit)
        if digit == 0:
            return "0"
        elif digit == 1:
            return nums[::-1]

        l = len(nums)
        ans = ""
        i = 0
        carry = 0
        while i<l:
            cur = int(nums[i])*digit + carry
            carry = cur//10
            ans += str(cur%10)
            i+=1

        if carry:
            ans += str(carry)

        ans = ans[::-1]
        i=0
        l = len(ans)
        while i<l and ans[i] == "0":
            i+=1        
        if ans[i:]:
            return a[i:]
        return "0"




    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        sign = 1
        if num1[0] == "-":
            sign = -1*sign
            num1 = num1[1:]
        if num2[0] == "-":
            sign = -1*sign
            num2 = num2[1:]
        result = "0"
        num1 = num1[::-1]
        c=0
        for d in num1:
            mult = self.multiply_digit(num2, d) + "0"*c
            # print(d, num2, mult, self.add(ans, mult))
            print(d, num2, self.add(result, mult))
            result = self.add(result, mult)
            print("result:", result)
            c+=1
        if sign == -1 and result != "0":
            result = "-"+result
        return result


s=Solution()
# print(s.add("0", "400"))
# print(s.multiply_digit("424", "8"))
a=str(141)
b=str(123)
print(s.multiply(a,b), int(a)*int(b))