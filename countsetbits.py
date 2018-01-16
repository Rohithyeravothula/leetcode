import math
class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        a=[0]*(1+(10**6))

        def check_prime(n):
        	if n<2:
        		return False
        	elif n==2 or n==3:
        		return True
        	m = int(math.sqrt(n)) + 1
        	for i in range(2, m):
        		if n%i==0:
        			return False
        	return True

        def set_bits(n):
        	c=0
        	while n:
        		c+=1
        		n=n&(n-1)
        	return c

        count = 0
        for i in range(L, R+1):
        	if check_prime(set_bits(i)):
        		count += 1
        return count

s=Solution()
print(s.countPrimeSetBits(0,1000000))