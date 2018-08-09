def search(a, start, end, target):
    a_end = end
    a_start = start
    while start <= end:
        mid = (start + end) >> 1
        if mid > a_start and a[mid] > target and a[mid-1] < target:
            return mid
        elif mid < a_end-1 and a[mid] < target and a[mid+1] > target:
            return mid+1
        elif a[mid] == target:
            return mid
        elif target > a[mid]:
            start = mid + 1
        else:
            end = mid-1
    return -1

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l = len(nums)
        ans = 1 # length of longest increasing subsequence
        opt = [-1*float("inf")]*l
        opt[0] = nums[0]
        for i in range(1, l):
            if nums[i] > opt[ans-1]:
                opt[ans] = nums[i]
                ans += 1
            elif nums[i] < opt[0]:
                opt[0] = nums[i]
            else:
                r = search(opt, 0, ans-1, nums[i])
                opt[r] = nums[i]
        return ans

search([2,4,8], 0, 2, 7)
# inp = []
# s = Solution()
# print(s.lengthOfLIS(inp))
