class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        i = 0
        j = l-1
        ans = 0
        while i<l and j>=0:
            # print(i, j)
            if i==j or i==j-1:
                break
            elif i == j-2:
                if nums[i+1] > nums[i] and nums[i+1] > nums[j]:
                    ans = i+1
                else:
                    break
            m = int((i+j+1)/2)
            if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                ans = m
                break
            elif nums[m-1] <= nums[i]:
                j = m+1
            else:
                i = m-1
        return ans

a=[1,2,3,1]
s=Solution()
print(s.findPeakElement(a))