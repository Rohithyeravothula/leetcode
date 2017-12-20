class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        l = len(cost)
        if l == 0:
            return 0
        elif l < 2:
            return min(a)
        zero_opt = [float("inf")]*(l+1)
        zero_opt[0] = 0
        zero_opt[1] = cost[0]
        zero_opt[2] = cost[1]
        for i in range(3, l+1):
            zero_opt[i] = min(zero_opt[i-1], zero_opt[i-2]) + cost[i-1]
        return min(zero_opt[l], zero_opt[l-1])

a = [0,0,0,0]
s = Solution()
print(s.minCostClimbingStairs(a))