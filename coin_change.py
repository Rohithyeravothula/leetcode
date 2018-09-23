class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        opt = [float("inf")]*(amount+1)
        opt[0] = 0
        for a in range(1, amount+1):
            for d in coins:
                if a < d:
                    break
                opt[a] = min(opt[a], 1+opt[a-d])
        return opt[amount]

s = Solution()
s.coinChange([2,3], 4)