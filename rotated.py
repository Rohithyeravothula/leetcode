class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        
        i=0
        j=l-1
        ri = -1

        while i>=0 and j<l and i<j:
            print(i, j)
            m=int((i+j)/2)

            if i == j-1 and nums[i] > nums[j]:
                ri = j
            
            if(m>0 and m<l and nums[m] < nums[m-1] and nums[m] < nums[m+1]):
                ri = m

            if(nums[i] >= nums[m]):
                j=m

            elif(nums[m] > nums[j]):
                i=m

            else:
                break

        print(ri)
        if(ri != -1):
            return nums[ri]

        else:
            return nums[0]

a=[5,6,7,8,1,2,3,4]
s = Solution()
print(s.findMin(a))