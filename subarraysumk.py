class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d={0:1}
        rs = 0
        ans = 0
        for i in nums:
            rs += i
            if rs-k in d:
                ans += d[rs-k]
            if rs in d:
                d[rs] += 1
            else:
                d[rs] = 1
        return ans

a=[1,2,3,2,3,2,3]
s=Solution()
print(s.subarraySum(a,115))