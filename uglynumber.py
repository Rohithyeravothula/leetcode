import math
class Solution(object):
	def isUgly(self, num):
		"""
		:type num: int
		:rtype: bool
		"""
		if num == 0:
			return False
		while num%5==0:
			num = num/5
		while num%3==0:
			num = num/3
		while num%2==0:
			num = num/2
		return num == 1
	def nthUglyNumber(self, n):
		t1=0
		t2=0
		t3=0
		ans = [float("inf")]*(max(n, 5))
		ans[0] = 1
		for i in range(1, n):
			ans[i] = min(ans[t1]*2, ans[t2]*3, ans[t3]*5)
			if ans[i] == ans[t1]*2:
				t1+=1
			if ans[i] == ans[t2]*3:
				t2+=1
			if ans[i] == ans[t3]*5:
				t3+=1
		return ans[n-1]


s=Solution()
# for i in range(1, 20):
print(s.nthUglyNumber(1900))