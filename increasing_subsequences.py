class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        def recr(nums, i, l):
            if i==l-1:
                return [[nums[i]]]
            sol = recr(nums, i+1, l)
            resol = []
            repeated = []
            curmax = 0
            for a in sol:
                if nums[i] < a[0]:
                    resol.append([nums[i]] + a)
                elif nums[i] == a[0]:
                    j=0
                    while j<len(a) and a[j] == nums[i]:
                        j+=1
                    if j>curmax:
                        repeated = [a]
                        curmax = j
                    elif j==curmax:
                        repeated.append(a)
                if len(a) > 1 or a[0] != nums[i]:
                    resol.append(a)
            for a in repeated:
                resol.append([nums[i]] + a)
            resol.append([nums[i]])
            return resol

        ans = recr(nums, 0, len(nums))
        return [a for a in ans if len(a) >= 2]

test = [4,8,1,2]
test = [4,6,7,7]
# test = [1,2,3,4]
# test = [1,2,1,1]
print(Solution().findSubsequences(test))