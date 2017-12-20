class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        profits = [0]*l
        for i in range(1, l):
            profits[i] = max(0, prices[i] - prices[i-1])
        return sum(profits)

prices = []
s=Solution()
print(s.maxProfit(prices))