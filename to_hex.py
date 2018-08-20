class Solution(object):
    def to_hex(self, num):
        hex_map = {i:str(i) for i in range(10)}
        hex_map.update({10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'})
        s = ""
        while num:
            s += hex_map[num % 16] 
            num = num//16
        return s[::-1]


    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        return self.to_hex(num)

s = Solution()
print(s.toHex(34))