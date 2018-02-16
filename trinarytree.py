class Node(object):  # Please do not remove or rename any of this code
    """Represents a single node in the Ternary Search Tree"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.mid = None
        self.right = None

    def __repr__(self):
        return str("node: ", self.val)

class Tree(object):  # Please do not remove or rename any of this code
    """The Ternary Search Tree"""
    def __init__(self):
        self.root = None
    
    
    def insert_helper(self, head, val):
        if head is None:
            return Node(val)
        elif val < head.val:
            head.left = self.insert_helper(head.left, val)
        elif val > head.val:
            head.right = self.insert_helper(head.right, val)
        elif val == head.val:
            head.mid = self.insert_helper(head.mid, val)
        return head

    # Please complete this method.
    """Inserts val into the tree. There is no need to rebalance the tree."""
    def insert(self, val):
        self.root = self.insert_helper(self.root, val)

    def delete_side(self, node, side, newnode):
        if side==1:
            node.right = newnode
        else:
            node.left = newnode

    def inorder_successor(self, head):
        cur = head 
        while cur.left is not None:
            cur = cur.left
        return cur
    
    def delete_helper(self, parent, current,val, side):
        """
        1) get inorder successor if right is not None
        2) parent pointer needs to be maintained
        3) if no right and mid sub trees, copy left node val
        4) if leaf node, parent side null
        right=+1
        left=-1
        """
        if current is None:
            return None

        if val == current.val:
            if current.left is None and current.right is None and current.mid is None:
                self.delete_side(parent, side, None)
            
            elif current.right is None and current.mid is None:
                self.delete_side(parent, side, current.left)

            elif current.mid is not None:
                p = current
                n = current.mid.mid
                while n is not None:
                    p = p.mid
                    n = n.mid 
                p.mid = None
            elif current.right is not None:
                ino_succ = self.inorder_successor(current.right)
                current.val = ino_succ.val
                self.delete_helper(current, current.right, ino_succ.val, 1)

        elif val < current.val:
            self.delete_helper(current, current.left, val, -1)
        elif val > current.val:
            self.delete_helper(current, current.right, val, +1)



        
        

    # Please complete this method.
    """Deletes only one instance of val from the tree.
       If val does not exist in the tree, do nothing.
       There is no need to rebalance the tree."""
    def delete(self, val):
        if val == self.root.val:
            if self.root.left is None and self.root.right is None and self.root.mid is None:
                self.root = None
            elif self.root.mid is None and self.root.right is None:
                self.root = self.root.left
            elif self.root.mid is not None:
                self.delete_helper(None, self.root, val, 0)
            elif self.root.right is not None:
                ino_succ = self.inorder_successor(self.root.right)
                self.root.val = ino_succ.val
                self.delete_helper(self.root, self.root.right, ino_succ.val, 1)
        else:
            if val < self.root.val:
                self.delete_helper(self.root, self.root.left, val, -1)
            elif val > self.root.val:
                self.delete_helper(self.root, self.root.right, val, +1)
        


def inorder(head):
    if head is None:
        return 
    else:
        inorder(head.left)
        print(head.val)
        inorder(head.mid)
        inorder(head.right)



        
t = Tree()
t.insert(20)
t.insert(20)
t.insert(10)
t.insert(10)
t.insert(10)
t.insert(8)
t.insert(30)
t.insert(40)
t.insert(35)

def delete(t, val):
    print("before")
    inorder(t.root)
    t.delete(val)
    print("after")
    inorder(t.root)


delete(t, 40)
# print(t.root, t.root.left, t.root.right)