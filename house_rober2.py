class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def simple_rob(houses):
            h1, h2, h = 0, 0, 0
            l = len(houses)
            for i in range(l):
                h = max(h1, h2+houses[i])
                h2=h1
                h1=h
            return h
        return max(simple_rob(nums[1:]), simple_rob(nums[2:-1])+nums[0])

s = Solution()
print(s.rob([2,1]))


[1,2,null,3,4,1,null,2,3,1,null,1,1,2,null,3,3,4,1,null,null,null,null,null,1,2,3]
[1,2,3,4,1,2,3,1,1,1,2,3,3,4,1,1,2,3]
