# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def tostr(a):
            return "->".join(list(map(lambda x: str(x), a)))
        def get_paths(root):
            if root is None:
                return []
            else:
                left = get_paths(root.left)
                right = get_paths(root.right)
                paths = left + right
                if not paths:
                    return [[root.val]]
                sol = []
                for p in paths:
                    p.append(root.val)
                    sol.append(p)
                return sol
        paths = get_paths(root)
        # print(paths)
        result = []
        for path in paths:
            result.append(tostr(path[::-1]))
        return result

from graph import *

t=leetcode_tree([37,-34,-48,None,-100,-100,48,None,None,None,None,-54,None,-71,-22,None,None,None,8])
s=Solution()
print(s.binaryTreePaths(t))
