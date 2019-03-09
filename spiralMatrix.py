class Solution:
    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        if not matrix:
            return []
        l = len(matrix)
        if l==1:
            return matrix[0]
        b = len(matrix[0])
        rl, rr, cs, ce = 0, b-1, 0, l-1
        ans = []
        while rl <= rr and cs <= ce:
            if rl == rr and cs == ce:
                ans.append(matrix[rl][cs])
                break
            elif rl == rr:
                for i in range(cs, ce+1):
                    ans.append(matrix[i][rl])
                break
            elif cs == ce:
                for i in range(rl, rr+1):
                    ans.append(matrix[cs][i])
                break
            else:
                for i in range(rl, rr+1):
                    ans.append(matrix[cs][i])

                for i in range(cs+1, ce+1):
                    ans.append(matrix[i][rr])

                for i in range(rr-1, rl-1, -1):
                    ans.append(matrix[ce][i])

                for i in range(ce-1, cs, -1):
                    ans.append(matrix[i][cs])
            rl+=1
            rr-=1
            cs+=1
            ce-=1
        return ans
inp = [[1,2,3,4], [2,3,4,5],[3,4,5,2]]
inp = [[1,2,3], [4,5,6]]
inp = [[1],[2],[3]]
inp = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().spiralOrder(inp))
