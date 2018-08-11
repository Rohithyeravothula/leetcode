class Solution:
    def shortestPathAllKeys(self, grid_str):
        """
        :type grid: List[str]
        :rtype: int
        """
        grid = [list(i) for i in grid_str]
        start_state = 0
        keys = {'a', 'b', 'c', 'd', 'e', 'f'}
        locks = {'A', 'B', 'C', 'D', 'E', 'F'}
        continue_symbols = {"@", "#"}
        answer_state = (1 << 7) -1
        pos_state = {}
        l = len(grid)
        b = len(grid[0])
        for i in range(l):
            for j in range(b):
                if grid[i][j] == "@":
                    break

        def get_positions(x, y):
            next_pos = {(x+1, y), (x, y+1), (x-1, y), (x, y-1)}
            return next_pos

        cur = [(i, j, start_state, 0)]
        while cur:
            cur_new = []
            for x, y, s, stp in cur:
                for nx, ny in get_positions(x, y):
                    next_state = None
                    if grid[nx][ny] in keys:
                        key_bit = ord(grid[nx][ny]) - ord('a') + 1
                        newstate = s | (1 << key_bit)
                        if newstate == answer_state:
                            return "found"
                        next_state = (nx, ny, newstate, 1+stp)

                    elif grid[nx][ny] == "@":
                        next_state = (nx, ny, s, 1+stp)

                    elif grid[nx][ny] in locks and s & (1 << (ord(grid[nx][ny]) - ord('A') + 1)):
                        next_state = (nx, ny, s, 1+stp)

                    if next_state:
                        if (nx, ny, s) in pos_state and pos_state[(nx, ny, s)] > 1+stp:
                            cur_new.append(next_state)
                            pos_state[(nx, ny, s)] = 1 + stp
                        else:
                            cur_new.append(next_state)
                            pos_state[(nx, ny, s)] = 1 + stp
            cur = cur_new
        return -1

s = Solution()
g = ["@.a.#","###.#","b.A.B"]
print(s.shortestPathAllKeys(g))
