from collections import defaultdict
from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1: return 1
        seen = defaultdict(set)
        for x,y in trust:
            seen[x].add(y)
        seen = {key:len(val) for key, val in seen.items()}
        found = None
        for key in range(1, n+1):
            if key not in seen:
                if found is None:
                    found = key
                else:
                    return -1
        return -1 if found is None else found


n, inp = 3, [[1,3],[2,3]]
n, inp = 2, [[1,2],[2,1]]
n, inp = 2, [[1,2]]
n, inp = 4, [[1,3],[2,3],[3,1]]
n, inp = 4, [[1,3],[1,4],[2,3],[2,4],[4,3]]
n, inp = 3, [[1,2],[2,3]]
print(Solution().findJudge(n, inp))
