class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        l = len(nums)
        s = sum(nums)
        if s < abs(target):
            return 0
        s_range = (2*s)+1
        opt = [[0]*(s_range) for _ in range(l)]
        for i in range(s_range):
            if i-s == nums[0]:
                opt[0][i] += 1
            if i-s == -1*nums[0]:
                opt[0][i] += 1
        

        for i in range(1, l):
            for j in range(0, s_range):
                if j >= nums[i]:
                    opt[i][j] += opt[i-1][j-nums[i]]
                if j+nums[i] < s_range:
                    opt[i][j] += opt[i-1][j+nums[i]]

        # for row in opt:
        #     print(row)
        return opt[l-1][s+target]

print(Solution().findTargetSumWays([0,0,1], 1))