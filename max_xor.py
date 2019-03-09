class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get(s0, s1, i):
            # print(i)
            if i<0:
                if s0 and s1:
                    return s0[0] ^ s1[0]
                return 0
                
            s00, s01, s10, s11 = [], [], [], []
            for num in s0:
                s01.append(num) if (num>>i & 1) else s00.append(num)

            for num in s1:
                s11.append(num) if (num>>i & 1) else s10.append(num)

            return max(get(s00, s11, i-1), get(s01, s10, i-1))
        s0, s1 = [], []
        for num in nums:
            s1.append(num) if (num>>32 & 1) else s0.append(num)
        return get(s0, s1, 31)


inp = [1,2,3,4,5]
s = Solution()
print(s.findMaximumXOR(inp))
                    
