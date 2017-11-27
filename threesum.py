class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l=len(nums)
        d={}
        nums.sort()
        for i in range(0, l):
            c=-1*nums[i]
            d[c] = i

        print(nums)
        print(d)
        i=0
        j=1
        tripletes = []
        while i<l:
            j=i+1
            if j>=l:
                break
            while j<l-1:
                if nums[j] == nums[j+1]:
                    j+=1
                else:
                    break
            c=nums[i]+nums[j]
            print(i, j, c)
            if c in d and d[c] > j:
                tripletes.append([nums[i], nums[j], c*-1])
            i+=1
        return tripletes

a=[1,1,-2]
s=Solution()
print(s.threeSum(a))