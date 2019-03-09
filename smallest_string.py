class Solution:
    def smallestFromLeaf(self, root: 'TreeNode') -> 'str':
        orda = ord('a')
        a = {i:chr(orda+i) for i in range(25)}
        if not root:
            return None
        cur = [(root, "")]
        leaf = None
        while cur:
            nxt = []
            for node, rep in cur:
                if not node.left and not node.right:
                    if not leaf:
                        leaf = a[node.val] + rep
                    else:
                        leaf = min(leaf, a[node.val]+rep)
                if node.left:
                    nxt.append((node.left, a[node.val]+rep))
                if node.right:
                    nxt.append((node.right, a[node.val]+rep))
            cur = nxt
        return leaf

Solution().smallestFromLeaf(None)



