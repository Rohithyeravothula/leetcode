import math
class Solution(object):
    def countPrimes(self, number):
        """
        :type n: int
        :rtype: int
        """
        if number < 2:
        	return 0
        nums = [1]*number
        nums[0] = 0
        nums[1] = 0
        half = 1+int(math.sqrt(number))
        for i in range(2, half):
        	for j in range(2*i, number, i):
        		nums[j] = 0
        # print([i for i in range(0, number) if nums[i] == 1])
        return sum(nums)

s=Solution()
s.countPrimes(19)