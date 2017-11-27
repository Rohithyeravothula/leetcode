class Solution:
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        def count(a):
            c = 0
            for i in a:
                if i=='0':
                    c+=1
            return c, len(a)-c
        opt = [[0] * (n+1) for _ in range(0, m+1)]
        for z,o in [count(s) for s in strs]:
            for j in range(m, -1, -1):
                for k in range(n, -1, -1):
                    if z <= j and o <= k:
                        opt[j][k] = max(opt[j][k], 1+opt[j-z][k-o])
            # print(opt)
        return opt[m][n]

strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
s=Solution()
print(s.findMaxForm(strs, m, n))