class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l = len(nums)
        opt = [[0,0]]*l # length, count
        opt[0] = [1,1]
        for i in range(1, l):
            max_length = 1
            count = 0
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if opt[j][0] > max_length:
                        max_length, count = opt[j]
                    elif opt[j][0] == max_length:
                        count += opt[j][1]
            # if no number is smaller than current one
            if count == 0:
                opt[i] = [1, 1]
            else:
                opt[i] = [1+max_length, count]
        # print(opt)
        max_length = max(opt, key=lambda x: x[0])[0]
        return sum([c for l, c in opt if l == max_length ])


inp = [1]
s = Solution()
print(s.findNumberOfLIS(inp))
