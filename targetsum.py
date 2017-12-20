import math
class Solution(object):
    def findTargetSumWays(self, allnums, target):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if len(allnums)==0:
            return 0

        nums = list(filter(lambda x: x != 0, allnums))
        S=2*sum(list(map(lambda x: abs(x), nums)))

        l = len(nums)
        nums.sort()
        zero_count = len(allnums) - len(nums)
        # print(S//2, target)
        ans = 0
        if abs(target) == abs(S//2):
            ans = 1
        elif abs(target) < -1*abs(S//2) or abs(target) > abs(S//2):
            return 0
        else:
            count = [[0]*(S+1) for _ in range(0, l+1)]
            count[0][S//2] = 1
            for i in range(1, l+1):
                for j in range(1, S+1):
                    cur = 0
                    if j-nums[i-1] >= 0 and j-nums[i-1] < S:
                        cur = count[i-1][j-nums[i-1]] 
                    if j+nums[i-1] >= 0 and j+nums[i-1] < S:
                        cur += count[i-1][j+nums[i-1]]
                    count[i][j] = cur
            # for c in count:
            #     print(c)
            ans = count[l][target+(S//2)]
        return ans*int(math.pow(2, zero_count))

a=[1,0]
t= 1
s=Solution()
print(s.findTargetSumWays(a, t))