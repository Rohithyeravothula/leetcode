class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        i,j,cur_sum,min_length=0,0,0,l+1
        while i<l and j<l:
            # print(i, j)
            while j<l:
                cur_sum += nums[j]
                j+=1
                if cur_sum >= s:
                    break
            if cur_sum < s:
                break
            min_length = min(min_length, j-i)
            while i<j:
                cur_sum -= nums[i]
                i+=1
                if cur_sum >= s:
                    min_length = min(min_length, j-i)
                else:
                    break
        if min_length == l+1:
            return 0
        return min_length


print(Solution().minSubArrayLen(16, [2,3,1,2,4,3]))
