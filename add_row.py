class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        cur = [root]
        while cur and d > 2:
            nxt = []
            for node in cur:
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            cur = nxt
            d-=1
        for node in cur:
            l1 = TreeNode(v)
            l1.left = node.left
            node.left = l1
            l2 = TreeNode(v)
            l2.right = node.right
            node.right = l2
        return root

from graph import TreeNode, inorder, leetcode_tree
s = Solution()
t = leetcode_tree([1,2,3,4,5,6,7,8])
print(inorder(t))
ut = s.addOneRow(t, 3, 2)
print(inorder(ut))
