class Solution:
    def isIdealPermutation(self, a):
        """
        :type A: List[int]
        :rtype: bool
        """
        info = []
        l = len(a)
        for i in range(0, l):
        	info.append([a[i], i])
        info.sort()
        i = 1
        while i<l:
        	if info[i][1]-info[i-1][0] > 1:
        		return False
        return True

s=Solution()
print(s.isIdealPermutation())
