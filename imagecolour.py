class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        l = len(image)    
        b = len(image[0])
        visited = [[0] * b for _ in range(0, l)]
        oldColour = image[sr][sc]
        stack = [[sr, sc]]
        while len(stack) != 0:
            i,j = stack.pop()
            if i<l and i>=0 and j<b and j>=0 and visited[i][j] == 0 and image[i][j] == oldColour:
                image[i][j] = newColor
                stack.append([i+1, j])
                stack.append([i-1, j])
                stack.append([i, j+1])
                stack.append([i, j-1])
                visited[i][j] = 1
        return image

def printMatrix(a):
    for i in a:
        print(i)

test = [[1,1,1],[0,1,1],[1,0,1]]
s=Solution()
ans = s.floodFill(test, 1,1, 2)
printMatrix(ans)

