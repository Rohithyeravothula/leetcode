class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        level = root
        while level is not None:
            cur = level
            while cur is not None:
                if cur.left is not None:
                    cur.left.next = cur.right
                if cur.right is not None and cur.next is not None:
                    cur.right.next = cur.next.left
                cur = cur.next
            level = level.left




from graph import *
s=Solution()
t=leetcode_tree([i for i in range(0, 31)])
s.connect(t)
tree_next(t)