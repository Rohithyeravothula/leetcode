from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1],[1,1]]
        if numRows < 3:
            return ans[:numRows]
        for i in range(3, numRows+1):
            cur = [1]
            n = i-1
            for j in range(1, n+1):
                cur.append(cur[-1]*(n-j+1)//j)
            ans.append(cur)
        return ans

inp = 4
print(Solution().generate(inp))
