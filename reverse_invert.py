class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        def reverse(a):
            la = len(a)
            l = la>>1
            for i in range(l):
                a[i], a[l-i-1] = a[l-i-1], a[i]
            for i in range(l):
                a[i] = a[i]^1
        
        for row in A:
            reverse(row)
        return A

inp = [[1,1,0]]
Solution().flipAndInvertImage(inp)