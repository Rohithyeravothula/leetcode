class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        def computer(a, i, j):
        	if i>=j or i==j-1:
        		return 0
        	elif i == j-2:
        		if a[i+1] <= a[i] and a[i+1] <= a[j]:
        			return min(a[i], a[j]) - a[i+1]
        		return 0
        	m = max(a[i:j+1])
        	mi = a[i:j+1].index(m)
        	return max(computer(a, i, m), computer(a, m, j))
        return computer(height, 0, len(height)-1)
hts = [3,0,3,4]
print(Solution().trap(hts))