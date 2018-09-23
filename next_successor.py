from graph import *
class Node():
	def __init__(self, val):
		self.val = val
		self.left, self.right, self.parent = None, None, None

	def __repr__(self):
		return str(self.val)


class BinaryTreeWithParent():
	def __init__(self, val):
		self.root = Node(val)

	def inorder_successor(self, node):
		if not node:
			return None
		if node.right:
			p = node.right
			while p.left:
				p = p.left
			return p
		else:
			parent = node.parent
			current = node
			while parent:
				if parent.left == current:
					return parent
				else:
					current = parent
					parent = parent.parent
			return parent



bt = BinaryTreeWithParent(1)
t=bt.root

t.left = Node(2)
t.left.parent = t
t.right = Node(3)
t.right.parent = t
t.right.right = Node(4)
t.right.right.parent = t.right
t.right.left = Node(5)
t.right.left.parent = t.right
print(bt.inorder_successor(t.right.left))