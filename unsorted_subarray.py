class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [(val, i) for i,val in enumerate(nums)]
        nums.sort()
        l = len(nums)
        i,j=0,l-1
        while i<l and nums[i][1] == i:
            i+=1
        while j>=i and nums[j][1] == j:
            j-=1

        return j-i+1 if j>=i else 0


inp = [1,2,3,4,5]
inp = [2, 6, 4, 8, 10, 9, 15]
inp = [2,4,4,8,10,9,15]
inp = []
print(Solution().findUnsortedSubarray(inp))
