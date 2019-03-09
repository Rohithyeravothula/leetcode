from typing import List

from collections import defaultdict
class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        def get_val(x,y):
            d = str(y-x)
            ds = str(x+y)
            x,y = str(x), str(y)
            return ["r"+x, "c"+y, "d"+d, "ds"+ds]
        def get_adjacent(x, y, n):
            children = [(x,y),(x+1,y),(x-1,y),(x,y+1),(x,y-1),(x+1,y+1),(x+1,y-1),(x-1,y+1),(x-1,y-1)]
            return [(i,j) for i, j in children if (i>=0 and i<n) and (j>=0 and j<n)]


        pos = defaultdict(int)
        lamp_pos = set()
        for x,y in lamps:
            for key in get_val(x,y):
                pos[key] += 1
            lamp_pos.add((x,y))
        ans = []
        for x,y in queries:
            # print(pos)
            found = False
            for key in get_val(x, y):
                if pos[key] > 0:
                    ans.append(1)
                    found = True
                    break
            if not found:
                ans.append(0)
            for child in get_adjacent(x,y,n):
                i,j = child
                if (i,j) in lamp_pos:
                    for key in get_val(i, j):
                        if pos[key] > 0:
                            pos[key] -= 1
                    lamp_pos.remove((i,j))
        return ans
n, lamps, queries = 5, [[1,1], [1,0]], []
print(Solution().gridIllumination(n, lamps, queries))
