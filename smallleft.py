class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = [[num, idx] for idx, num in enumeration(nums)]
        a.sort()
        l = len(nums)
        ans = [0]*l
        for i in range(0, l):
        	if i > a[i][1]:
        		ans[i] = i - a[i][1]
        return ans


nms = [5,2,6,1]
s=Solution()
print(s.countSmaller(nms))

