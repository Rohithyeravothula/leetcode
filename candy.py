class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        s1 = sum(A)
        s2 = sum(B)
        d = (s1-s2) >> 1
        s = set(A)
        for i,v in enumerate(B):
            if v+d in s:
                return [v+d, v]

aa = [1,2,5]
bb = [2]
s = Solution()
print(s.fairCandySwap(aa, bb))