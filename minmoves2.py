class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        m = min(nums)
        m2 = max(nums) 
        for i in range(0, l):
            if nums[i] > m and nums[i] < m2:
                m2 = nums[i]

        ans = 0
        for i in nums:
            if i == m:
                ans += m2-i
            else:
                ans += i-m2
        return ans
s=Solution()
print(s.minMoves2([1,5,1]))
        