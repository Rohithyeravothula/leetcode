class Solution:
    def combinationSum4(self, nums: 'List[int]', target: 'int') -> 'int':
        opt = [0]*(target+1)
        opt[0] = 1
        for i in range(1, target+1):
            for val in nums:
                if val <= i:
                    opt[i] += opt[i-val]
        return opt[target]

inp, t = [], 4
print(Solution().combinationSum4(inp, t))
