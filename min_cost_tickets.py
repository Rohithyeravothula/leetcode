class Solution:
    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
        l = len(days)
        ans = [0]*(l+1)
        for i in range(l):
        	cost = ans[i]+costs[0] # one day pass
        	j = i
        	# print(days[i], cost)
        	while j>0 and days[i]-days[j-1] < 7:
        		# print(days[i], ans[j-1]+costs[1],  days[i]-days[j])
        		cost = min(cost, ans[j-1]+costs[1])
        		j-=1
        	j=i
        	while j>0 and days[i]-days[j-1] < 30:
        		cost = min(cost, ans[j-1]+costs[2])
        		j-=1
        	ans[i+1] = cost
        # print(ans)
        return ans[-1]

s = Solution()
inp, cst = [1,2,3], [1,2,0]
inp, cst = [1,4,6,7,8],[2,7,15]
inp, cst = [1,4,6,7,8,20],[2,7,15]
inp, cst = [1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]
inp, cst = [1,2,3,4],[1,1,1]
print(s.mincostTickets(inp, cst))