class Solution(object):
    def combisum(self, candidates, target):
        if target == 0:
            return [[]]
        elif not candidates or target < candidates[0]:
            return None
        l = len(candidates)
        ans = []
        prev = None
        for i in range(0, l):
            if candidates[i] != prev:
                sol = self.combisum(candidates[i+1:], target-candidates[i])
                if sol is not None:
                    updated = list(map(lambda x: [candidates[i]] + x, sol))
                    ans.extend(updated)
                prev = candidates[i]
        return ans

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = self.combisum(candidates, target)
        if ans is not None:
            return ans
        return []

s=Solution()
print(s.combinationSum2([1,1,1,1,1,1,1,1,1], 8))