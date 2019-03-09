class Solution:
    def floodFill(self, image: 'List[List[int]]', sr: 'int', sc: 'int', newColor: 'int') -> 'List[List[int]]':
        def get_children(x,y,color,l,b):
            ans = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
            ans = [(i,j) for i, j in ans if ((i>=0 and i<l) and (j>=0 and j<b))]
            return [(i,j) for i,j in ans if image[i][j] == color]

        l = len(image)
        b = len(image[0])
        cur = [(sr, sc)]
        color = image[sr][sc]
        image[sr][sc] = -1
        while cur:
            nxt = []
            for x,y in cur:
                for cx, cy in get_children(x,y, color, l, b):
                    image[cx][cy] = -1
                    nxt.append((cx, cy))
            cur = nxt
        for i in range(l):
            for j in range(b):
                if image[i][j] == -1:
                    image[i][j] = newColor
        return image




image = [[0,0,0],[0,1,1]]
sr = 1
sc = 1
newColor = 1

image = [[0,0,0],[0,1,0]]
sr = 1
sc = 1
newColor = 2

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2

print(Solution().floodFill(image, sr, sc, newColor))
