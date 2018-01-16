class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        right_profit = [0]*l
        right_max = prices[l-1]
        max_profit = 0
        for i in range(l-2, -1, -1):
        	right_profit[i] = max(max_profit, right_max - prices[i])
        	max_profit = right_profit[i]
        	right_max = max(right_max, prices[i])

        opt = [0]*l
        for i in range(1, l):
            for j in range(0, i):
                if j+2<l:
                    opt[i] = max(opt[i], opt[j]+right_profit[j+2])
            opt[i] = max(opt[i], opt[i-1])
            opt[i] = max(opt[i], opt[i-2])
        return opt[n-1]

prs = [100, 10, 20, 5, 100, 180]
s=Solution()
s.maxProfit(prs)