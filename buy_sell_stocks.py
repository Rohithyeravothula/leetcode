class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        if not prices:
            return 0
        l = len(prices)
        buy = [0]*(l+1)
        profit = [0]*(l+1)
        buy[1] = -prices[0]
        for i in range(2, l+1):
            buy[i] = max(buy[i-1], profit[i-2] - prices[i-1])
            profit[i] = max(profit[i-1], buy[i-1]+prices[i-1])
        # print(prices)
        # print(buy[1:])
        # print(profit[1:])
        return profit[-1]

prices = [1,2]
print(Solution().maxProfit(prices))
