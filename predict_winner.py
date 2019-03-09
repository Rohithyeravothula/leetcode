from typing import List


def pprint_list(a):
    for row in a:
        print(row)
class Solution:
    def PredictTheWinner(self, a: List[int]) -> bool:
        l = len(a)
        s = sum(a)
        score = [[0]*l for _ in range(l)]
        for i in range(l):
            score[i][i] = a[i]
        for i in range(l-1):
            score[i][i+1] = max(a[i], a[i+1])
        pprint_list(score)
        for k in range(2, l):
            for i in range(l-k):
                j = i+k
                score[i][j] = max(a[i]+min(score[i+1][j-1], score[i+2][j]), a[j]+min(score[i+1][j-1], score[i][j-2]))
        pprint_list(score)
        return score[0][l-1] >= (s+1)//2

inp = [1,3,1]
print(Solution().PredictTheWinner(inp))

while not True:
    inp = list(map(int, input().split()))
    print(Solution().PredictTheWinner(inp))
