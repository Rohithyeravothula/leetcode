class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        l = len(heights)
        i = 0
        stk = []
        max_area = 0
        while i<l:
            # print(stk)
            if not stk:
                stk.append(i)
            else:
                if heights[i] > heights[stk[-1]]:
                    stk.append(i)
                else:
                    while stk and heights[stk[-1]] > heights[i]:
                        top = stk.pop()
                        if stk:
                            max_area = max(max_area, heights[top]*(i-stk[-1]-1))
                        elif not stk:
                            max_area = max(max_area, heights[top]*i)
                    stk.append(i)
            i+=1
        # print(stk)
        while stk:
            top = stk.pop()
            if stk:
                max_area = max(max_area, heights[top]*(i-stk[-1]-1))
            else:
                max_area = max(max_area, heights[top]*i)
        return max_area

inp = [2,1,5,6,2,3]
inp = [4,1,4,1,1]
inp = [4,2,0,3,2,5]
print(Solution().largestRectangleArea(inp))
        