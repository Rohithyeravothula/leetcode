class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        l = len(nums)
        triplets = []
        print(nums)
        for i in range(l-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            start = i+1
            end = l-1
            while start < end:
                cur_sum = nums[i] + nums[start] + nums[end]
                if cur_sum == 0:
                    triplets.append([nums[i], nums[start], nums[end]])
                    while start < end and nums[start] == nums[start+1]:
                        start += 1
                    while end > start and nums[end] == nums[end-1]:
                        end -= 1
                    start += 1
                    end -= 1
                elif cur_sum < 0:
                    start += 1
                else:
                    end -= 1
        return triplets

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))


