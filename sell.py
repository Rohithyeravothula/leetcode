class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """ 
        buy=0
        sell=0
        profit = 0
        l=len(prices)
        current = 1
        while current < l:
            print(buy, sell, current)
            if prices[buy] > prices[current]:
                buy = current
                sell = current
            if prices[current] > prices[sell]:
                sell = current
                curProfit = prices[sell] - prices[buy]
                if curProfit > profit:
                    profit = curProfit
            current += 1
        return profit





# a=[4,2,1,5,2,1,4,5,1,2,4]
a=[7,6,5,4,3,2]
s=Solution()
s.maxProfit(a)