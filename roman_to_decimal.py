class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        exceptions = {4:"IV", 9:"IX", 40:"XL", 90:"XC", 400:"CD", 900:"CM"}
        roman_keys = [1,5,10,50,100,500,1000, 10000]
        romans = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M', 10000:'-1'}
        response = []
        p = 10
        while (10*num)//p > 0:
            cur = num%p
            num = (num//p)*p
            p *= 10
            cur_response = []
            print(cur, end=", ")
            while cur:
                if cur in exceptions:
                    cur_response.append(exceptions[cur])
                    break
                for index, value in enumerate(roman_keys):
                    if value > cur:
                        break
                cur_response.append(romans[roman_keys[index-1]])
                cur = cur - roman_keys[index-1]
            print(cur_response)
            response.append("".join(cur_response))
        response = response[::-1]
        return "".join(response)

s = Solution()
print(s.intToRoman(4123))



            