class Solution:
    def findPeakElement(self, a):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = [-1*float("inf")] + a + [-1*float("inf")]
        l = len(a)
        i = 1
        j = l-2
        while i<=j:
        	m = (i+j) >> 1
        	# print(i, j, m)
        	if a[m] > a[m-1] and a[m] > a[m+1]:
        		return m-1
        	elif a[m] > a[m-1]:
        		i = m+1
        	else:
        		j = m-1
        if a[1] > a[2]:
        	return 0
        else:
        	return l-3

s = Solution()
print(s.findPeakElement([1,2,1,3,5,6,4]))

