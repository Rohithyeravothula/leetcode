class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        for i in range(l):
        	index = abs(nums[i])
        	if index <= l and index > 0 and nums[index-1] > 0:
        		nums[index-1] *= -1

        response = []
        for i in range(l):
        	if nums[i] > 0:
        		response.append(i+1)
        return response

ary = [1,3,2]
s = Solution()
print(s.findDisappearedNumbers(ary))


