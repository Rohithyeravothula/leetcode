class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def divide(current):
        	l = len(current)
        	if l < 3:
        		return False
        	m = l//2
        	left = current[0:m+1]
        	middle = current[m]
        	right = current[m:]
        	if min(left) < middle < max(right):
        		return True
        	return divide(left) or divide(right)
        return divide(nums)

s=Solution()
print(s.increasingTriplet([]))
