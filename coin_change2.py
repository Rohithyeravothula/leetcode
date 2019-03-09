class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if not coins:
        	return 0
        l = len(coins)
        opt = [[0]*(amount+1) for _ in range(l)]
        for i in range(l):
            opt[i][0] = 1
        
        for j in range(1, amount+1):
            if coins[0] <= j:
                opt[0][j] = opt[0][j-coins[0]]
        
        
        for i in range(1, l):
            for j in range(1, amount+1):
                opt[i][j] = opt[i-1][j]
                if coins[i] <= j:
                    opt[i][j] += opt[i][j-coins[i]]
        # [print(row) for row in opt]
        return opt[l-1][amount]

a, c = 5, [1,2,5]
a,c = 3,[10]
a,c=10,[10]
a,c=4,[]
print(Solution().change(a, c))