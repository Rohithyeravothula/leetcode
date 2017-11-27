class Solution(object):
	def findSubsequences(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		def subseq(nums):
			print(nums)
			if len(nums) == 1:
				return [[nums[0]]]
			else:
				top = nums[-1]
				seqs = subseq(nums[:-1])
				cur = []
				for s in seqs:
					cur.append(s)
					if s[-1] <= top:
						cur.append(s+[top])
				cur.append([top])
				return cur
		ans = subseq(nums)
		for i in ans:
			if len(i) < 2:
				del ans[ans.index(i)]
		return ans

s = Solution()
a=[4,5,7,7]
print(s.findSubsequences(a))