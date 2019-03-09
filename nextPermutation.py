class Solution:
    def nextPermutation(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        def find(nums, val, l):
            i = l-1
            while i>=0 and nums[i] <= val:
                i-=1
            return i

        def reverse(nums, s, e):
            c = (1+e-s)//2
            for _ in range(c):
                nums[s], nums[e] = nums[e], nums[s]
                s+=1
                e-=1

        l = len(nums)
        i = l-1
        while i>0 and nums[i] <= nums[i-1]:
            i-=1
        if i>0:
            i-=1
            j = find(nums, nums[i], l)
            nums[i], nums[j] = nums[j], nums[i]
            reverse(nums, i+1, l-1)
        else:
            reverse(nums, 0, l-1)

inp = [1,2,3]
inp = [3,2,1]
inp = [2,3,1]
inp = [3,1,2]
inp = [4,2,5,1]
inp = [10,12,15]
inp = [5,1,1]
Solution().nextPermutation(inp)
print(inp)
