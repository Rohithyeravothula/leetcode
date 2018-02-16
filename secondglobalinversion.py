class Solution:
    def isIdealPermutation(self, a):
        """
        :type A: List[int]
        :rtype: bool
        """
        l = len(a)
        for i in range(0, l):
            if abs(a[i] - i) > 1:
                return False
        return True

s=Solution()
print(s.isIdealPermutation([1,0,2]))
