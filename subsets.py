class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def get_subsets(s):
            if not s:
                return [[]]
            val = s[0]
            ss = get_subsets(s[1:])
            ans = []
            for st in ss:
                ans.append(st)
                ans.append([val] + st)
            return ans
        return get_subsets(nums)
        