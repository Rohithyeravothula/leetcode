inf = float('inf')
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        l = len(dominoes)
        left = []
        dist = inf
        for val in dominoes:
            if val == 'R':
                dist = 0
            elif val == 'L':
                dist = inf
            else:
                dist += 1
            left.append(dist)
        right = []
        dist = inf
        for val in dominoes[::-1]:
            if val == 'L':
                dist = 0
            elif val == 'R':
                dist = inf
            else:
                dist += 1
            right.append(dist)
        right = right[::-1]
        # print(left)
        # print(right)

        ans = []
        for index, val in enumerate(dominoes):
            if val == ".":
                if left[index] != inf and right[index] != inf:
                    if left[index] == right[index]:
                        ans.append(".")
                    elif left[index] < right[index]:
                        ans.append("R")
                    else:
                        ans.append("L")
                elif left[index] != inf:
                    ans.append("R")
                elif right[index] != inf:
                    ans.append("L")
                else:
                    ans.append(val)
            else:
                ans.append(val)
        return "".join(ans)


inp = ".L.R...LR..L.."
# print(inp)
while True:
    inp = input()
    print(Solution().pushDominoes(inp))
