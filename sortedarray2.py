class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        if l<=1:
            return l
        prev = nums[0]
        i=1
        c=1
        total = 1
        ans = [nums[0]]
        while i<l:
            if nums[i] == prev and c<2:
                i+= 1
                total += 1
                c+=1
                ans.append(nums[i])
            elif nums[i] == prev and c>=2:
                c+=1
                i+=1
            else:
                prev = nums[i]
                i+=1
                total += 1
                ans.append(nums[i])
        nums=ans

a=[]
s=Solution()
print(nums)