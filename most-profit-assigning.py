from collections import defaultdict
class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        profit_range = (10**5)+10
        difficulty_map = defaultdict(int)
        for i, d in enumerate(difficulty):
        	difficulty_map[d] = max(difficulty_map[d], profit[i])
        profit_list = []
        curprofit = 0
        for i in range(0, profit_range):
        	profit_list.append(max(curprofit, difficulty_map[i]))
        	curprofit = max(curprofit, profit_list[i])

        max_profit = 0
        for w in worker:
        	max_profit += profit_list[w]
        return max_profit



# df = [2,2,6,8,10]
# pf = [10,20,30,40,50]
# ww=  [3]

df = [6,8,14,19,20,26,26,26,28,48,59,68,71,72,83,85,91,92,93,97]
pf = [18,24,26,28,38,41,43,47,57,60,62,65,75,77,79,81,88,92,93,95]
ww = [2,61,4,55,43,82,35,30,35,3,78,55,94,15,9,13,35,29,34,97]

s = Solution()
print(s.maxProfitAssignment(df, pf, ww))

