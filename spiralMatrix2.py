class Solution:
    def generateMatrix(self, n:'int'):
        if n==0:
            return []
        l,b = n,n
        matrix = [[0]*b for _ in range(l)]
        rl, rr, cs, ce = 0, b-1, 0, l-1
        cur = 1
        while rl <= rr and cs <= ce:
            if rl == rr and cs == ce:
                matrix[rl][cs] = cur
                cur += 1
                break
            elif rl == rr:
                for i in range(cs, ce+1):
                    matrix[i][rl] = cur
                    cur += 1
                break
            elif cs == ce:
                for i in range(rl, rr+1):
                    matrix[cs][i] = cur
                    cur += 1
                break
            else:
                for i in range(rl, rr+1):
                    matrix[cs][i] = cur
                    cur += 1

                for i in range(cs+1, ce+1):
                    matrix[i][rr] = cur
                    cur += 1

                for i in range(rr-1, rl-1, -1):
                    matrix[ce][i] = cur
                    cur += 1

                for i in range(ce-1, cs, -1):
                    matrix[i][cs] = cur
                    cur += 1
            rl+=1
            rr-=1
            cs+=1
            ce-=1
        return matrix
print(Solution().spiralOrder(5))
