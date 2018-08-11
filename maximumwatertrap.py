class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # print(height)
        if len(height) == 3:
            return max(0, min(height[0], height[2]) - height[1])
        elif len(height) <= 2:
            return 0
        else:
            max_h = height[1]
            max_i = 1
            l = len(height)
            # print(1, l-2)
            for i in range(1, l-1):
                if max_h < height[i]:
                    max_h = height[i]
                    max_i = i
            if max_h < height[0] and max_h < height[l-1]:
                min_h = min(height[0], height[l-1])
                water = 0
                for i in height[1:-1]:
                    water += min_h - i
                return water
            return self.trap(height[0:max_i+1]) + self.trap(height[max_i:])



# hts = [0,1,0,2,1,0,1,3,2,1,2,1]
hts = [1,0,1]
s=Solution()
print(s.trap(hts))