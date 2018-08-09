class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        opt = [[0]*l for _ in range(l)]
        for i in range(0, l):
            opt[i][i] = nums[i]

        for i in range(l-1):
            opt[i][i+1] = max(nums[i], nums[i+1])

        k=2
        while k<l:
            for i in range(l-k):
                j = i+k
                i_choice = nums[i] + min(opt[i+1][j-1], opt[i+2][j])
                j_choice = nums[j] + min(opt[i][j-2], opt[i+1][j-1])
                opt[i][j] = max(i_choice, j_choice)
            k+=1

        score = sum(nums)
        half_score = (score >> 1) + (score % 2)
        if opt[0][l-1] >= half_score:
            return True
        return False
inp = [1,5,233,7]
s = Solution()
print(s.PredictTheWinner(inp))
