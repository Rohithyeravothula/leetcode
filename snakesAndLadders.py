from math import ceil
class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        def get_children(pos, l):
            # print("children: ", pos)
            return [(pos+i, get_position(pos+i, l)) for i in range(1, 7) if pos+i <= l*l]

        def get_position(s, l):
            r = ceil(s/l)
            if r&1:
                return l-r, s-((r-1)*l)-1
            else:
                return l-r, l-(s-((r-1)*l))

        l = len(board)
        cur = set([(1,0)])
        seen = {}
        ans = float("inf")
        counter = 0
        while cur and ans == float("inf") and counter < l*l:
            # print(cur)
            counter += 1
            newcur = set()
            for pos, cost in cur:
                if pos == l*l:
                    ans = min(ans, cost)
                for update_pos, (child_i, child_j) in get_children(pos, l):
                    if board[child_i][child_j] != -1:
                        if board[child_i][child_j] in seen:
                            if seen[board[child_i][child_j]] > 1+cost:
                                seen[board[child_i][child_j]] = 1+cost
                                newcur.add((board[child_i][child_j], 1+cost))
                        else:
                            newcur.add((board[child_i][child_j], 1+cost))
                    else:
                        if update_pos in seen:
                            if seen[update_pos] > 1+cost:
                                seen[update_pos] = cost+1
                                newcur.add((update_pos, cost+1))
                        else:
                            newcur.add((update_pos, cost+1))
                            seen[update_pos] = 1+cost
            cur = newcur
        # print(ans)
        if ans == float("inf"):
            return -1
        return ans


# inp = [
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,35,-1,-1,13,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,15,-1,-1,-1,-1]]
# inp = [[-1,7,-1],[-1,6,9],[-1,-1,2]]
inp = [[1,1,-1],[1,1,1],[-1,1,1]]
Solution().snakesAndLadders(inp)


# 1 1 -1
# 1 1 1
# -1 1 1