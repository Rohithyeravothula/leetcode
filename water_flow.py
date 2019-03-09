class Solution:
    def pacificAtlantic(self, matrix: 'List[List[int]]') -> 'List[List[int]]':
        if not matrix:
            return []
        l = len(matrix)
        b = len(matrix[0])

        def get_children(node):
            x,y=node
            c = [(x+1,y), (x,y+1), (x-1,y), (x,y-1)]
            c = [(i,j) for i,j in c if ((i>=0 and i<l) and (j>=0 and j<b))]
            return [(i,j) for i,j in c if matrix[i][j] <= matrix[x][y]]

        def dfs(node, pe, te, re):
            print(node, pe)
            if node in re:
                return True
            if node in te:
                return False
            pe.add(node)
            result = False
            for child in get_children(node):
                if child not in pe:
                    cur = dfs(child, pe, te, re)
                    if cur:
                        result = True
                        re.add(node)
            pe.remove(node)
            te.add(node)
            return result
        
        pacific = set()
        atlantic = set()
        for i in range(l):
            pacific.add((i,0))
            atlantic.add((i,b-1))
        for j in range(b):
            pacific.add((0,j))
            atlantic.add((l-1,j))

        ppe,pte,ape,ate=set(),set(),set(),set()
        print(pacific)
        for i in range(l):
            for j in range(b):
                if (i,j) not in pacific:
                    dfs((i,j), ppe, pte, pacific)
                # if (i,j) not in atlantic:
                    # dfs((i,j), ape, ate, atlantic)
        print(pacific)
        print(atlantic)
        return list(pacific.intersection(atlantic))


from pprint import pprint
inp = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
pprint(inp)
print(Solution().pacificAtlantic(inp))