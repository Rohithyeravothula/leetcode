class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.extend(nums)
        l = len(nums)
        i =0
        ans = [-1]*(l//2)
        j=0
        stk = []
        while i<l:
            if len(stk) == 0:
                stk.append(i)
            else:
                top = stk[-1]
                if nums[top] < nums[i]:
                    if top < l//2:
                        ans[top] = nums[i]
                    stk.pop()
                else:
                    stk.append(i)
                    i+=1
        return ans

s=Solution()
print(s.nextGreaterElements([1,2,1]))


