class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
    	ans = 0
    	while n:
    		c = n&1
    		ans = ans | c
    		n = n >> 1
    		ans = ans << 1
    	ans = ans >> 1
    	ans = ans & 0xffffffff
    	return ans


a=7
s=Solution()
print(bin(a))
print(bin(s.reverseBits(a)))