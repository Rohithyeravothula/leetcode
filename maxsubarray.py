class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get(a,i,j):
            if i>j:
                return -float('inf')
            elif i==j:
                return a[i]
            else:
                m = i + (j-i)//2
                left = get(a, i, m)
                right = get(a, m+1, j)
                leftmax, rightmax = a[m], 0
                cur = a[m]
                for c in range(m-1, i-1, -1):
                    cur += a[c]
                    leftmax = max(leftmax, cur)
                cur = 0
                for c in range(m+1, j+1):
                    cur += a[c]
                    rightmax = max(rightmax, cur)
                span = leftmax + rightmax
                return max([left, right, span])
        l = len(nums)
        return get(nums, 0, l-1)

s = Solution()
inp = [1,2,3,4,5]
inp = [-1]
inp = [10,-4,2,1,3]
print(s.maxSubArray(inp))