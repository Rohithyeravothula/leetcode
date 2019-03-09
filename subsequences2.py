class Solution:
    def findSubsequences(self, nums: 'List[int]') -> 'List[List[int]]':
        ans = []
        for num in nums:
            cur = []
            for sub in ans:
                if sub[-1] < num:
                    cur.append(sub[:] + [num])
                    cur.append(sub)
                elif sub[-1] == num:
                    cur.append(sub[:] + [num])
                else:
                    cur.append(sub)
            cur.append([num])
            ans = cur
        return  [l for l in ans if len(l) > 1]

inp = [1,2,2,3]
print(Solution().findSubsequences(inp))

