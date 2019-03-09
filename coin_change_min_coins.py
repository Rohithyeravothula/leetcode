class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
            return -1
        l = len(coins)
        # coins.sort()
        opt = [float("inf")]*(amount+1)
        opt[0] = 0
        for a in range(1, amount+1):
            for c in coins:
                if c > a:
                    break
                opt[a] = min(opt[a], 1+opt[a-c])
        
        if opt[amount] == float("inf"):
            return -1
        return opt[amount]

c,a = [474,83,404,3], 264
c,a = [47,8,40,1], 27
c,a = [5,2,4,1], 4
print(Solution().coinChange(c, a))