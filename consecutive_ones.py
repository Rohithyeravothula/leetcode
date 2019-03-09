from typing import List


class Solution:
    def longestOnes(self, a: List[int], k: int) -> int:
        l = len(a)
        start, end = 0, 0
        ans = 0
        count = 0
        while start < l:
            # print(start, end, count)
            while end < l:
                if a[end] == 0:
                    count += 1
                    if count > k:
                        break
                end += 1
            # if end == l and (a[end-1] == 1 or count <= k):
                # end += 1
            ans = max(ans, end-start)
            while start < l and a[start] != 0:
                start += 1
            start += 1
            count -= 1
            end += 1
        return ans

inp,k = [1,1,1,0,0,0,1,1,1,1,0],2
inp,k = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3
inp,k = [1,1,0],1
print(Solution().longestOnes(inp,k))
