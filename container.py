class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        def area(i, j):
            return abs(min(height[i], height[j])*(i-j))

        l=len(height)
        s=0
        e=l-1
        maxarea = area(s, e)
        while s<e and s<l and e>=0:
            if height[s] < height[e]:
                s+=1
            else:
                e-=1
            curarea=area(s, e)
            if curarea > maxarea:
                maxarea = curarea
        return maxarea

a=[1,2,3,4,5,6]
s = Solution()
print(s.maxArea(a))



