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

    path_max = 0
    for vertex in range(0, n):
        stack = [[vertex,0]]
        # curmax = 0
        visited = [0]*n
        while len(stack) != 0:
            # print(stack)
            cur,path_length = stack.pop()
            if path_length > path_max:
                path_max = path_length
            visited[cur] = 1
            children = get_children(adj, cur, n)
            # print(children, n)
            for c in children:
                if visited[c] == 0 and  A[c] == A[cur]:
                    stack.append([c, path_length+1])
    return path_max


# a = [2,1,1,2,1,1]
# b = [1,2,2,3,2,4,2,5,5,6]
# ans = solution(a,b)
# print(ans)

# a = [1,2,3,4,5,6]
# b = [1,2,1,3]
# ans = solution(a,b)
# print(ans)


# a = [1,1,1,2,2]
# b = [1,2,1,3,2,4,2,5]
# ans = solution(a,b)
# print(ans)

# a=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# b=[1,2,2,3,3,4,1,5,1,6]
# ans = solution(a,b)
# print(ans)

# a=[1,1,1,1,1,1]
# b=[1,2,2,3,3,4,4,5]
# ans = solution(a,b)
# print(ans)

a=[1,2,1,2]
b=[1,2,1,3,1,4]
ans = solution(a,b)
print(ans)