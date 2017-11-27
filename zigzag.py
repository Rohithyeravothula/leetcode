class Solution(object):
	def convert(self, s, numRows):
		"""
		:type s: str
		:type numRows: int
		:rtype: str
		"""
		if(numRows == 1):
			return s
		ans=""
		i = 0
		l = len(s)
		while i<numRows:
			# print(i)
			b=0
			while True:
				m = 2*b*(numRows-1)
				pre = m-i
				# print(b, m, pre, l, m<l)   
				if(pre >= l):
					break

				if(i != 0 and i != numRows-1):
					if pre < l and pre > 0:
						ans += s[pre]

				if(m+i<l):
					ans += s[m+i]

				b+=1
			i+=1
		print(ans)
		return s

s = Solution()
# while True:
# 	x = input()
# 	s.convert(x, 1)

print(s.convert("abc", 1))