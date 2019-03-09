class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root

        if not root.left and not root.right and root.val == key:
            return None

        def remove_leav(cur, prev):
            if prev.left and prev.left.val == cur.val:
                prev.left = None
            else:
                prev.right = None


        cur = root
        prev = None
        while cur and cur.val != key:
            prev = cur
            cur = cur.right if cur.val < key else cur.left


        # not found
        if not cur:
            return root

        if not cur.left and not cur.right:
            # print(prev, cur)
            remove_leav(cur, prev)
            return root

        if not cur.left:
            # print("hmm")
            cur.val = cur.right.val
            cur.left = cur.right.left 
            cur.right = cur.right.right
            return root
        if not cur.right:
            cur.val = cur.left.val
            cur.right = cur.left.right
            cur.left = cur.left.left
            return root

        curright = cur.right
        curparent = cur
        while curright.left:
            curparent = curright
            curright = curright.left
        
        if curparent == cur:
            cur.right = None
        cur.val = curright.val
        if not curright.right:
            # print("removing", curright, curparent)
            remove_leav(curright, curparent)
        else:
            curright.val = curright.right.val
            curright.left = curright.right.left
            curright.right = curright.right.right
        return root

from graph import leetcode_tree, inorder
t = leetcode_tree([10, 5, 15, 3, 6, 12, 20])
t = leetcode_tree([2,None,3])
Solution().deleteNode(t, 2)
print(inorder(t))