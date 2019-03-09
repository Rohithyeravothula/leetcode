class Solution:
    def isCousins(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
        self.xp = None
        self.xl = None
        self.yp, self.yl = None, None
        def build(cur, k, parent):
            if cur:
                if cur.val == x:
                    self.xp, self.xl = parent, k
                if cur.val == y:
                    self.yp, self.yl = parent, k
                build(cur.left, k+1, cur)
                build(cur.right, k+1, cur)
        build(root, 0, None)
        return ((self.xl == self.yl) and (self.xp != self.yp))

from graph import leetcode_tree
t = leetcode_tree([1,2,3,4,5,6,7])
print(Solution().isCousins(t, 5,3))