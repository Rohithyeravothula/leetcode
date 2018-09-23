class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        i = 0
        m = 0
        while i<l:
            cur_i = i
            c = 0
            while nums[cur_i] >= 0:
                next_i = nums[cur_i]
                nums[cur_i] = -1
                cur_i = next_i
                c+=1
            m = max(c, m)
            i+=1
        return m
s = Solution()
print(s.arrayNesting([4,1,2,0,3]))