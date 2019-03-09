class Solution:
    def shortestSubarray(self, a: 'List[int]', k: 'int') -> 'int':
        seen = {a[0]:-1}
        counter = 0
        ans = float('inf')
        for i,val in enumerate(a[1:]):
            if val == k:
                return 1
            curkey = k-counter-val
            if curkey in seen:
                ans = min(ans, i-seen[curkey]+1)
            counter += val
            val = val - counter
            seen[val] = i
        return -1 if ans == float('inf') else ans


inp,k = [2,-1, 2], 3
inp,k = [1,2,3,4,8,9], 5
inp,k = [1,2,3,4,5,6,4], 100
inp,k = [1,2,3], 4
print(Solution().shortestSubarray(inp, k))
