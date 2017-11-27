class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def printRight(root, visited, ans, level):
            print(visited, ans, level)
            if root is None:
                return None

            if level not in visited:
                ans.append(root.val)
                visited[level] = 1            
            printRight(root.right, visited, ans, level+1)
            printRight(root.left, visited, ans, level+1)

        v={}
        a=[]
        printRight(root, v, a, 0)
        return a

t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
s = Solution()
print(s.rightSideView(t))