class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}
        i = 0
        l = len(nums)
        while i<=k and i<l:
            if nums[i] in seen:
                return True
            seen[nums[i]] = 1
            i+=1
        
        j=0
        while i<l:
            if seen[nums[j]] > 0:
                seen[nums[j]] -= 1
            if nums[i] in seen and seen[nums[i]] > 0:
                return True
            seen[nums[i]] = 1
            i+=1
            j+=1
        return False
                
print(Solution().containsNearbyDuplicate([1], 8))
        