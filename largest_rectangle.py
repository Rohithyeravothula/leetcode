class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        stk = [0]
        i = 1
        l = len(heights)
        max_area = heights[0]
        while i<l:
            if heights[stk[-1]] < heights[i]:
                stk.append(i)
            else:
                while stk and heights[stk[-1]] > heights[i]:
                    top = stk.pop()
                    if stk:
                        max_area = max(max_area, heights[top]*(i - stk[-1] -1))
                    else:
                        max_area = max(max_area, heights[top]*(i))
                stk.append(i)
            i+=1
        while stk:
            top = stk.pop()
            if stk:
                max_area = max(max_area, heights[top]*(i-stk[-1]-1))
            else:
                max_area = max(max_area, heights[top]*i)
        return max_area

inp = [4,2,0,3,2,5]
inp = [1,2,3][::-1]
inp = [1,1,1,1,1,0,4,0]
print(Solution().largestRectangleArea(inp))

