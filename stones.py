from typing import List

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        # print(stones)
        l = len(stones)
        if l==1:
            return 0
        if l < k:
            return -1
        if l==k:
            return sum(stones)
        curmax = sum(stones[:k])
        cur_indices = [(0, k-1)]
        cursum = curmax
        for i in range(k, l):
            cursum += stones[i]
            cursum -= stones[i-k]
            if cursum < curmax:
                curmax = cursum
                cur_indices = [(i-k+1, i)]
            elif cursum == curmax:
                cur_indices.append((i-k+1, i))
        # print(curmax, curstart, curend)
        localmin = float("inf")
        # print(cur_indices)
        for curstart, curend in cur_indices:
            newstones = stones[:curstart] + [curmax] + stones[curend+1:]
            newval = self.mergeStones(newstones, k)
            if newval == -1:
                return -1
            else:
                localmin = min(localmin, curmax + newval)
        return localmin


inp = [3,5,1,2,6]
inp = [4,6,9]
inp = [1]
inp = [5,4,1]
inp = [3,2,5]
inp = [3,2,4,1]
inp = [4,6,4,7,5]
inp = [69,39,79,78,16,6,36,97,79,27,14,31,4]
print(Solution().mergeStones(inp, 2))
