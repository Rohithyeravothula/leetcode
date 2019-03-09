class Solution:
    def maximumGap(self, nums: 'List[int]') -> 'int':
        if not nums:
            return 0
        def build(cur, i):
            l = len(cur)
            if l<2 or i==-1:
                return 0
            if l == 2:
                return abs(cur[0] - cur[1])
            left, right = [],[]
            for val in cur:
                if (val>>i)&1:
                    left.append(val)
                else:
                    right.append(val)
            left_val = build(left, i-1)
            right_val = build(right, i-1)
            curdiff = -float('inf')
            if left and right:
                curdiff = abs(max(right) - min(left))
            return max([left_val, right_val, curdiff])
        return build(nums, 31)

inp = [1,1,1,1,2,2,10]
print(Solution().maximumGap(inp))

