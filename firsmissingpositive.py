class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = float("inf")
        for i in nums:
            if i>=0 and m>i:
                m=i
        if m == float("inf"):
            return 1
        if m > 1:
            return 1
        l = len(nums)
        print(m)
        for i in range(0, l):
            nums[i] = float(nums[i])

        for i in range(0, l):
            if nums[i] >= 0:
                # if not updated 
                act = int(nums[i]) - m
                if act < l and act >= 0 and float(int(nums[act])) == nums[act]:
                        nums[act] = nums[act] + 0.5
        
        # print(a)
        is_break = False
        for i in range(0, l):
            if float(int(nums[i])) == nums[i]:
                is_break = True
                break
        if is_break:
            return m+i
        return m+i+1


a=[1,100]
s=Solution()
print(s.firstMissingPositive(a))