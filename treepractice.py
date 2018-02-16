class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


class DLLNode:
	def __init__(self, val):
		self.val = val
		self.next = None
		self.prev = None

class BinartTree:
	def __init__(self, val):
		self.root = TreeNode(val)

class BinarySearchTree:
	def __init__(self, val):
		self.root = TreeNode(val)

	def add(self, val):
		def __add(cur, val):
			if cur is None:
				return TreeNode(val)
			else:
				if cur.val < val:
					cur.right = __add(cur.right, val)
				else:
					cur.left = __add(cur.left, val)
				return cur
		__add(self.root, val)

	def inorder(self):
		def __inorder(cur):
			if cur is not None:
				__inorder(cur.left)
				print(cur.val)
				__inorder(cur.right)
		__inorder(self.root)

	def reverse(self):
		def reverse_(cur):
			if cur is not None:
				cur.left, cur.right = cur.right, cur.left
				reverse_(cur.left)
				reverse_(cur.right)
		reverse_(self.root)

	def check_mirror(self):
		def mirror(left, right):
			if left is None and right is None:
				return True
			elif left is None or right is None:
				return False
			elif left.val == right.val:
				return mirror(left.right, right.left) and mirror(left.left, right.right)
			return False

	def toLinkedList(self):
		def tll(cur):
			if cur is None:
				return None
			else:
				left_head, left_tail = tll(cur.left)
				right_head, right_tail = tll(cur.right)
				newnode = DLLNode(cur.val)

				if left_head:
					left_tail.next = newnode
					newnode.prev = left_tail
				else:
					left_head = newnode

				if right_head:
					newnode.next = right_head
					right_head.prev = newnode
				else:
					right_tail = newnode

				return left_head, right_tail

		return tll(self.root)[0]

bst = BinarySearchTree(1)
# bst.root.left = TreeNode(2)
# bst.root.right = TreeNode(3)

bst.add(2)
bst.add(3)
bst.inorder()
bst.reverse()
bst.inorder()
# print(bst.root.val)
