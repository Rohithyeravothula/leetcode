class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l =  len(prices)
        if l < 2:
            return 0
        min_price = prices[0]
        max_profit_i = [0]*l # max profit selling on day i
        for i in range(0, l):
            max_profit_i[i] = max(0, prices[i]-min_price)
            min_price = min(min_price, prices[i])

        # max_profit_cur = max_profit_i[0]
        # for i in range(0, l):
        #     max_profit_i[i] = max(max_profit_cur, max_profit_i[i])
        
        max_profit_j = [0]*l
        max_price = prices[l-1]
        for i in range(l-1, -1, -1):
            max_profit_j[i] = max(0, max_price - prices[i])
            max_price = max(max_price, prices[i])

        #print(max_profit_i)
        #print(max_profit_j)


        max_profit_cur = max_profit_j[l-1]
        for i in range(l-1, -1, -1):
            max_profit_j[i] = max(max_profit_cur, max_profit_j[i])
            max_profit_cur = max(max_profit_cur, max_profit_j[i])

        #print(max_profit_j)

        max_profit_cur = max(0, max(max_profit_i))
        for i in range(0, l-1):
            max_profit_cur = max(max_profit_cur, max_profit_i[i] + max_profit_j[i+1])

        return max_profit_cur



a=[1,40]
s=Solution()
print(s.maxProfit(a))