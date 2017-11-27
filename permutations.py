class Solution:
	def permute(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		def perm(a):
			if len(a) == 1:
				return [a]
			else:
				ans = []
				cur = perm(a[1:])
				num = a[0]
				for c in cur:
					l = len(c)
					for i in range(0, l+1):
						ans.append(c[0:i] + [num] + c[i:])
				return ans
		if len(nums) == 0:
			return []
		return perm(nums)

s=Solution()
print(s.permute([1,2,4,3]))
