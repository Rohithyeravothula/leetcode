class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
        	return 0
        max_h = height[0]
        max_i = 0
        l = len(height)
        for i in range(0, l):
        	if max_h < height[i]:
        		max_h = height[i]
        		max_i = i

        ans = 0
        left = height[0]
        for i in range(0, max_i):
        	if height[i] >= left:
        		left = height[i]
        	else:
        		ans += left - height[i]

        right = height[l-1]
        for i in range(l-1, max_i, -1):
        	if height[i] >= right:
        		right = height[i]
        	else:
        		ans += right - height[i]
        return ans


hts = [0,1,0,2,1,0,1,3,2,1,2,1]
s=Solution()
print(s.trap(hts))
