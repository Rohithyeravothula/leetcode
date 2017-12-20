class Solution(object):
    def combisum(self, candidates, target):
        if target == 0:
            return [[]]
        elif not candidates or target < candidates[0]:
            return None
        l = len(candidates)
        ans = []
        for i in range(0, l):
            sol = self.combisum(candidates[i:], target-candidates[i])
            if sol is not None:
                updated = list(map(lambda x: [candidates[i]] + x, sol))
                ans.extend(updated)
        return ans

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = self.combisum(candidates, target)
        if ans is not None:
            return ans
        return [[]]

s=Solution()
print(s.combisum([1,2,3,4,5], 7))