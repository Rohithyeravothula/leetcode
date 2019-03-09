class Solution:
    def isIdealPermutation(self, a):
        """
        :type A: List[int]
        :rtype: bool
        """
        l = len(a)
        for i in range(l):
            c = (i==0 and a[i]!=0 and a[i+1]!=0) and (i==l-1 and i!=a[i] and i!=a[i-1]) and (i!=a[i] and i!=a[i-1] and i!=a[i+1])
            if c:
                return False
        return True

inp = [0,1,2,3,4,5,10,9,8,7,6]
inp = [1,2,3,0,4,5,6]
inp = [0,3,1,2]
inp = [1,0,2]
inp = [1,2,0,3]
print(Solution().isIdealPermutation(inp))