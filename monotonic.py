class Solution:
    def isMonotonic(self, a):
        """
        :type A: List[int]
        :rtype: bool
        """
        tpe = None
        l = len(a)
        for i in range(1, l):
        	if a[i-1] < a[i]:
        		if not tpe:
        			tpe = "increasing"
        		elif tpe != "increasing":
        			return False
        	elif a[i-1] > a[i]:
        		if not tpe:
        			tpe = "decreasing"
        		elif tpe != "decreasing":
        			return False
        return True


s = Solution()
print(s.isMonotonic([]))