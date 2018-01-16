class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=1
        l = len(nums)
        if l == 0:
            return 0
        curpdt = nums[0]
        count = 0
        i=0
        j=1
        while i<=j or j<l:
            if curpdt <= s:
                if j>i+1:
                    count += 1
                if j<l:
                    curpdt *= nums[j]
                    j+=1
                else:
                    curpdt //= nums[i]
                    i+=1
            else:
                if nums[i] <= s:
                    count += 1
                curpdt //=nums[i]
                i+=1
        return count


a=[10,5,2,6]
s=Solution()
print(s.minSubArrayLen(100, a))