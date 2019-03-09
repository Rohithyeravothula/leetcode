from typing import List
class Solution:
    def largestSumOfAverages(self, a: List[int], k: int) -> float:
        def build(a, i, j, k, seen):
            print(i,j,k)
            print(seen)
            if i>j:
                return 0
            if (i, j, k) in seen:
                return seen[(i, j, k)]
            if k==1:
                cur = sum(a[i:j+1])/(j-i+1)
                seen[(i,j,k)] = cur
                return cur
            if i==j:
                cur = a[i]
                seen[(i,j,k)] = cur
                return cur
            cur = 0
            for r in range(i, j+1):
                nxt = build(a, r+1, j, k-1, seen)
                local = sum(a[i:r+1])/(r-i+1)
                cur = max(cur, nxt+local)
            seen[(i,j,k)] = cur
            return cur
        return build(a, 0, len(a)-1, k, {})

inp,k = [9, 1, 2, 3, 9], 3
inp,k = [9,9,9], 2
inp,k = [9,9],4
inp,k = [5,5],1
print(Solution().largestSumOfAverages(inp, k))
