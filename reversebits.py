class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        count = 32
        while count:
        	ans = ans << 1
        	ans = ans | (n&1)
        	n = n >> 1
        	count -= 1
        return ans


a=1
s=Solution()
print(bin(a))
print(bin(s.reverseBits(a)))
assert("0b"+bin(a)[2:][::-1] == bin(s.reverseBits(a)))