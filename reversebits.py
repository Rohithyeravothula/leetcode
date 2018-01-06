class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        r = 1<<32
        return r^n


a=0
s=Solution()
print(bin(a))
print(bin(s.reverseBits(a)))