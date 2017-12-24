class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        opt = [[0]*l for _ in range(0, l)]
        for i in range(0, l):
            opt[i][i] = nums[i]

        e=1
        while e<l:
            i=0
            j=e
            while i<l and j<l:
                print(i, j)
                for k in range(i, j):
                    opt_sol = opt[i][k-1]
                i+=1
                j+=1
            e+=1
        for a in opt:
            print(a)
        return opt[0][l-1]

blns = [3,1,5,8]
s=Solution()
s.maxCoins(blns)