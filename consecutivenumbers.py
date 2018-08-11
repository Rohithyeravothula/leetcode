class Solution:
	def consecutiveNumbersSum(self, N):
		"""
		:type N: int
		:rtype: int
		"""
		count = 1
		for i in range(1, N):
			if (i*(i+1)) >= 2*N:
				break
			numerator = (2*N - (i*(i+1)))
			denominator = (2*(i+1))
			a = numerator % denominator
			# print(a, i)
			if a == 0:
				count += 1
		return count

s=Solution()
print(s.consecutiveNumbersSum(15))
for i in range(20):
	print(i, s.consecutiveNumbersSum(i))