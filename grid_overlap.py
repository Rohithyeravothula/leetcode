# Complete the countMatches function below.

def get_children(grid, i, j, l, b):
    candidates = [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]
    children = []
    for u, v in candidates:
        if u < l and u >= 0 and v < b and v >= 0 and grid[u][v] != 0:
            children.append((u, v))
    return children


def countMatches(g1, g2):
    if not g1 or not g2:
        return 0
    l = min(len(g1), len(g2))
    b = min(len(g1[0]), len(g2[0]))
    if b == 0:
        return 0
    grid1 = [list(map(int, list(row))) for row in g1]
    grid2 = [list(map(int, list(row))) for row in g2]
    for i in range(l):
        for j in range(b):
            if grid2[i][j] == 1 and grid1[i][j] == 1:
                grid2[i][j] = 2
    # print(grid2)
    grid2_l = len(grid2)
    grid2_b = len(grid2[0])
    regions = 0
    visited = set()
    while True:
        cur = None
        for i in range(grid2_l):
            for j in range(grid2_b):
                if (i, j) not in visited and grid2[i][j] == 2:
                    cur = [(i, j)]
                    break
            if cur:
                break

        if not cur:
            break

        valid_region = True
        # print(cur)
        while cur:
            next = []
            for (cur_i, cur_j) in cur:
                children = get_children(grid2, cur_i, cur_j, grid2_l, grid2_b)
                for (child_i, child_j) in children:
                    if grid2[child_i][child_j] == 1:
                        valid_region = False
                    if (child_i, child_j) not in visited and grid2[child_i][child_j] != 0:
                        next.append((child_i, child_j))
                visited.add((cur_i, cur_j))
            cur = next
            # print(cur)
        if valid_region:
            regions += 1
    return regions


# g1 = ['']
# g2 = ['']

# g1 = ["111", "100", "100"]
# g2 = ["001", "001", "110"]


g2 = ["11", "00"]
g1 = ["111", "000"]
print(countMatches(g1, g2))
