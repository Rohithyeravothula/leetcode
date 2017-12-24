class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        def connect_right(lst, rst):
            if lst is None or rst is None:
                return None
            lst.next=rst
            connect_right(lst.left, lst.right)
            connect_right(lst.right, rst.left)
            connect_right(rst.left, rst.right)
        if root is not None and root.left is not None and root.right is not None:
            connect_right(root.left, root.right)