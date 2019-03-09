class Solution:
    def maxSubarraySumCircular(self, a):
        """
        :type A: List[int]
        :rtype: int
        """
        l = len(a)
        if l==1:
            return a[0]
        i = 0
        max_sum = a[0]
        while i<l:
            cur_sum = a[i]
            max_sum = max(max_sum, cur_sum)
            j = (i+1)%l
            while j!=i:
                cur_sum = max(cur_sum+a[j], a[j])
                max_sum = max(max_sum, cur_sum)
                if cur_sum == a[j]:
                    break
                j = (j+1)%l
            # print(i, j, max_sum)
            if j<=i:
                break
            i=j
        return max_sum

inp = [4]
inp = [-4]
inp = [5,-2,5]
inp = [1,2,3,4]
inp = [-3, -2, -1]
inp = [10,-4,8,-100]
inp = [10,-4,8,-100, 20]
print(Solution().maxSubarraySumCircular(inp))