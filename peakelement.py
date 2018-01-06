class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        i = 0
        j = l-1
        while i<=j:
            m = (i+j)//2
            if m == i:
                if nums[i] > nums[j]:
                    return i 
                return j
            if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                return m
            elif nums[m] < nums[m+1]:
                i = m+1
            else:
                j = m-1
    
        return l-1


a=[3,2,1,0]
s=Solution()
print(s.findPeakElement(a))