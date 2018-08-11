class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        def flip(lst):
            return [1 if l==0 else 0 for l in lst]
        l = len(A)
        if l == 0:
            return 0
        if l == 1:
            a1 = int("0b" + "".join([str(i) for i in A[0]]), 2)
            a2 = int("0b" + "".join([str(i) for i in flip(A[0])]), 2)
            return max(a1, a2)
        b = len(A[0])
        

        matrix = []
        for n in A:
            if n[0] == 0:
                matrix.append(flip(n))
            else:
                matrix.append(n)

        

        for j in range(1, b):
            zc = 0
            for i in range(0, l): 
                if matrix[i][j] == 0:
                    zc += 1
            if zc > l/2:
                for i in range(0, l):
                    if matrix[i][j] == 0:
                        matrix[i][j] = 1
                    else:
                        matrix[i][j] = 0
        ans = 0
        for n in matrix:
            lst = [str(i) for i in n]
            ans += int("0b" + "".join(lst), 2)
        return ans

s = Solution()
print(s.matrixScore([[0,0,1,1]]))

