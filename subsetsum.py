

# a[i][j] = can I get sum using first i elements

# a(i, j) = a(i-1, j-b[i]) || a(i-1, j)

class Solution(object):
	def canPartition(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		def printboard(a):
			for i in range(l):
				print(a[i])
			
		l = len(nums)
		s = sum(nums)
		if s%2 != 0:
			return False
		s = int(s/2)+1
		a=[]
		for i in range(0, l):
			a.append([0] * s)

		for i in range(0,l):
			a[i][0] = 1

		if nums[0]/2 < s:
			a[0][nums[0]] = 1

		printboard(a)
		print()
		# print(l, s)

		for i in range(1, l):
			for j in range(1, s):
				if nums[i] <= j:
					a[i][j] = a[i-1][j] or a[i-1][j-nums[i]]
				else:
					a[i][j] = a[i-1][j]
		printboard(a)
		return 1==a[l-1][s-1]

a=[2, 4]
s = Solution()
s.canPartition(a)