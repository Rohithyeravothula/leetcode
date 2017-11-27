# m = adj matrix, r = root, n = num of nodes
def get_children(m, r, n):
    children = []
    for i in range(0, n):
        if r != i and m[r][i] == 1:
            children.append(i)
    return children


def solution(A, E):
    n = len(A)
    adj = [[0] * n for _ in range(0, n)]
    l = len(E)
    #adj matrix
    for i in range(0, l, 2):
        adj[E[i]-1][E[i+1]-1] = 1
        adj[E[i+1]-1][E[i]-1] = 1

    path_max = 1
    stack = []
    visited = [0]*n
    while True:
        for i in range(0, n):
            if visited[i] == 0:
                stack.append(i)
                visited[i] = 1
                break
        if len(stack) == 0:
            break
        curmax = 1
        marked = [0]*n
        while True:
            # print(stack)
            cur = stack.pop()
            marked[cur] = 1
            children = get_children(adj, cur, n)
            for c in children:
                if marked[c] == 0 and  A[c] == A[cur]:
                    stack.append(c)
            if len(stack) == 0:
                break
            curmax += 1
        if curmax > path_max:
            path_max = curmax
    return path_max-1


a=[1,1,1,1]
b=[1,2,1,3,1,4]
ans = solution(a,b)
print(ans)
