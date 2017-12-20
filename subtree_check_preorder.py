def preorder_iterative(root):
    if root is None:
        return []
    stack = []
    ans = []
    p = root
    while not (len(stack) == 0 and  p is None):
        while p is not None:
            stack.append(p)
            ans.append(p.val)
            p = p.left
            if p is None:
                ans.append("#")

        while len(stack) != 0:
            p = stack.pop()
            p = p.right
            if p is not None:
                stack.append(p)
                break
            else:
                ans.append("#")
    return ans

from graph import *
t = get_skewed_tree(5)
print(preorder_iterative(t))


class Solution(object):

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        spreorder =  [ str(i) for i in preorder_iterative(s)]
        spreorder = "".join(spreorder)
        tpreorder = [ str(i) for i in preorder_iterative(t)]
        tpreorder = "".join(tpreorder)
        if t is None:
            return True
        elif tpreorder in spreorder:
            return True
        else:
            return False