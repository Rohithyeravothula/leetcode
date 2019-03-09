class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        s = sum(nums)
        if s&1:
            return False
        w = s>>1
        cur = [False]*(w+1)
        cur[0] = True
        for i in range(1, l+1):
            newcur = [False]*(w+1)
            newcur[0] = True
            for j in range(1, w+1):
                if j>=nums[i-1]:
                    newcur[j] = cur[j] or cur[j-nums[i-1]]

            cur = newcur

        # for row in opt:
            # print(row)
        return cur[w]

inp = [1,2,3,4,5]
inp = [1,11,5,5]
inp = []
print(Solution().canPartition(inp))
