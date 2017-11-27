class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l=len(nums)
        if l==0:
            return False
        a=[0]*l
        a[0] = nums[0]
        for i in range(1, l):
            a[i] = max(a[i-1]-1, nums[i])
        ans = True
        for i in range(0, l-1):
            if a[i] == 0:
                ans = False
                break
        return ans



a=[10,2,0,0,0,0,0,0,1]
s=Solution()
print(s.canJump(a))
