class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        s=0
        e=l-1
        ans = -1
        count = 0
        while s<e:
            count+=1
            if (count>10):
                break
            print(s,e)
            m=int((s+e)/2)
            if m==0 and nums[0] > nums[1]:
                ans = -1
                break
            else:
                s=int((l-1)/2)
                e=l-1

            if m==l-1 and nums[m-1] < nums[m]:
                ans = m
                break
            else:
                s=0
                e=int((l-1)/2)
            if s==e:
                break
            if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                ans = m
                break

            if nums[m] < nums[m-1] and nums[m] > nums[s]:
                e=m
            elif nums[m] < nums[m+1] and nums[m] < nums[e]:
                s=m

        if ans == -1:
            return 0
        return ans


s=Solution()
a=[1,2,3,1]
print(s.findPeakElement(a))
