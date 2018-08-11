from collections import defaultdict
class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """

        def largest_small(a, v, l):
            i = 0
            j = l-1
            if a[j] < v:
                return j 
            if a[i] > v:
                return -1

            ans = -1
            while i<j:
                m = (i+j)//2
                # print(i, j, m)
                if a[m] == v:
                    return m 
                elif a[m] < v:
                    i = m+1
                    ans = m
                else:
                    j = m-1
            if i == j and a[i] <= v:
                ans = i
            return ans

        if not difficulty:
            return 0



        start = list(zip(difficulty, profit))
        start.sort()
        dfp = []
        curprofit = 0
        for d, p in start:
            dfp.append((d, max(curprofit, p)))
            curprofit = max(curprofit, p)
        # print(dfp)




        # updated_profit = [profit[0]]
        # curprofit = profit[0]
        # for i, p in enumerate(profit):
        #     curprofit = max(curprofit, p)
        #     updated_profit.append(curprofit)

        # dfp = list(zip(difficulty, updated_profit))
        # dfp.sort()

        dfp_map = defaultdict(int)
        for d, p in dfp:
            dfp_map[d] = max(dfp_map[d], p)
        # print(dfp_map)

        dfp = list(dfp_map.items())
        dfp.sort()
        
        diffs = [d for (d, p) in dfp]
        prf = [p for (d, p) in dfp]
        difflen = len(diffs)
        # print(diffs)
        # print(prf)

        maxp = 0
        for w in worker:
            lw = largest_small(diffs, w, difflen)
            # print(w, lw, prf[lw])
            if lw != -1:
                maxp += prf[lw]
        return maxp








df = [2,4,6,8,10]
pf = [10,20,30,40,50]
ww = [4,5,6,7]

# df = [68,35,52,47,86]
# pf = [67,17,1,81,3]
# ww = [92,10,85,84,82]


# df = [6,8,14,19,20,26,26,26,28,48,59,68,71,72,83,85,91,92,93,97]
# pf = [18,24,26,28,38,41,43,47,57,60,62,65,75,77,79,81,88,92,93,95]
# ww = [2,61,4,55,43,82,35,30,35,3,78,55,94,15,9,13,35,29,34,97]

s = Solution()
print(s.maxProfitAssignment(df, pf, ww))

