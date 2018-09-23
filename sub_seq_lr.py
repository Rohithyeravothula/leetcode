class Solution(object):
    def numSubarrayBoundedMax(self, a, l, r):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        a = [val if val >= l and val <= r else -1 for val in a]
        print(a)
        l = len(a)
        i = 0
        ans = 0
        while i<l:
            count = 0
            while i<l and a[i] != -1:
                i+=1
                count += 1
            ans += max(0, ((count*count) - 1))
            i+=1
        print(ans)
        return ans
        
Solution().numSubarrayBoundedMax([2,1,4,3], 2, 3)