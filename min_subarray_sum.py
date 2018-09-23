class Solution(object):
    def sumSubarrayMins(self, a):
        """
        :type A: List[int]
        :rtype: int
        """
        i = 0
        l = len(a)
        count = 0
        m = (10**9) + 7
        while i<l:
        	j = i-1
        	while j>=0 and a[j] > a[i]:
        		j-=1
        	left = i-j
        	j = i+1
        	while j<l and a[j] >= a[i]:
        		j+=1
        	right = j-i
        	count = (count + (left*right)*a[i])%m
        	i+=1
        print(count)
        return count
inp = [1,2,3]
inp = [3,1,2,4]
inp = []
inp = [2,1,3,1]
inp = [71,55,82,55]
inp = [1,1,1,1]
Solution().sumSubarrayMins(inp)