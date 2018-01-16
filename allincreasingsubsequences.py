class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sol = []
        prev = -1
        l = len(nums)
        for i in range(0, l):
            tmp = []
            if prev != -1 and nums[prev] == nums[i]:
                j = -1*(i-prev)
                for t in sol:
                    if abs(j)<=len(t) and t[j] == nums[i]:
                        tmp.append(t+[nums[i]])
            else:
                for t in sol:
                    if t[-1] < nums[i]:
                        tmp.append(t+[nums[i]])
                tmp.append([nums[i]])
            sol.extend(tmp)
            if prev == -1 or nums[i] != nums[prev]:
                prev = i

        # print(sol)
        
        result = []
        for t in sol:
            if len(t) > 1:
                result.append(t)
        return result

s=Solution()
print(s.findSubsequences([1,2,1,1]))