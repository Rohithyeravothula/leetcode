from random import randint
from collections import deque

null = None

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

    def __str__(self):
    	return str(self.label)

    def __repr__(self):
    	return str(self)

class GraphNode:
	def __init__(self, x):
		self.label = x
		self.neighbors = []

	def __str__(self):
		return str(self.label)

	def __repr__(self):
		return str(self)

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None



class DoubleListNode:
    def __init__(self, val):
        self.val = val 
        self.next = None
        self.prev = None

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

def print_graph(root):
	queue = deque([root])
	visited = set()
	while queue:
		cur = queue.popleft()
		if cur not in visited:
			print(cur.label)
			print("children -> ", cur.neighbors)
			queue.extend(cur.neighbors)
			visited.add(cur)
	print("\n\n")


def graph_example():
	test = UndirectedGraphNode(1)
	_a = UndirectedGraphNode(2)
	_b = UndirectedGraphNode(3)
	# _c = UndirectedGraphNode(4)
	# _d = UndirectedGraphNode(5)
	test.neighbors = [_a, _b]
	_a.neighbors = [test, _b]
	_b.neighbors = [test, _a]
	# _c.neighbors = [ _d]
	# print_graph(test)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next=None

    def __str__(self):
        if self is not None:
            return str(self.val)
        else:
            return "None"

    def __repr__(self):
        return str(self)


def inorder(node):
	if node is None:
		return None
	inorder(node.left)
	print(node.val, end=", ")
	inorder(node.right)

def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    s1 = [root]
    s2 = []
    ans = []
    while len(s1) != 0 or len(s2)!=0:
        # print(s1, s2, ans)
        i_ans = []
        while len(s1)!=0:
            p = s1.pop()
            if p is not None:
                s2.append(p.right)
                s2.append(p.left)
                i_ans.append(p.val)
        if len(i_ans) != 0:
            i_ans = i_ans[::-1]
            ans.append(i_ans)
        i_ans = []
        # print(s1, s2, ans)
        while len(s2)!=0:
            p = s2.pop()
            if p is not None:
                s1.append(p.left)
                s1.append(p.right)
                i_ans.append(p.val)
        if len(i_ans) != 0:
            ans.append(i_ans)
        # print(s1, s2, ans)
    return ans


def get_graph():
    a=TreeNode(10)
    b=TreeNode(5)
    c=TreeNode(15)
    a.left = b
    # a.right = c
    return a


    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)
    h = TreeNode(8)
    a.left = b 
    a.right = c 
    b.left = d 
    b.right = h
    d.left = e
    e.left = f 
    f.left = g
    return a

def get_tree():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)
    h = TreeNode(8)
    a.left = b 
    a.right = c 
    b.left = d
    b.right = e 
    d.left = f 
    f.left = g
    g.left = h
    return a

def get_skewed_tree(n):
    start = TreeNode(1)
    cur = start
    for i in range(2, n):
        cur.right = TreeNode(i)
        cur = cur.right
    return start


def dist(u,v, d):
	if u is None:
		return float("inf")
	if u.val == v:
		return d
	else:
		return min(dist(u.left, v, d+1), dist(u.right, v, d+1))


def leetcode_tree(a):
    def __helper(a, i, n):
        if i>=n:
            return None
        else:
            if a[i] is None:
                return None
            cur = TreeNode(a[i])
            cur.left = __helper(a, 2*i+1, n)
            cur.right = __helper(a, 2*i+2, n)
            return cur
    return __helper(a, 0, len(a))

# print(inorder(leetcode_tree([1,2,3,4])))

def tree_next(root):
    def __helper(cur):
        if cur is None:
            return None
        elif cur is not None and cur.next is not None:
            print(cur.val, cur.next.val)
        else:
            print(cur.val, "None")
        __helper(cur.left)
        __helper(cur.right)
    __helper(root)

def get_ll(n):
    """
    returns linkedlist of range n
    """
    if n<1:
        return None
    head = ListNode(0)
    cur = head
    for i in range(1, n):
        newnode = ListNode(i)
        cur.next = newnode
        cur = cur.next
    return head

def get_rand_sorted_ll(n):
    if n<1:
        return None
    prev = randint(0, 9)
    head = ListNode(prev)
    cur = head
    for i in range(n):
        cur_val = randint(0, 9)
        prev += cur_val
        newnode = ListNode(prev)
        cur.next = newnode
        cur = cur.next
    return head

def get_rand_ll(n):
    if n<1:
        return None
    head = ListNode(randint(0, 9))
    cur = head
    for i in range(1, n):
        newnode = ListNode(randint(0, 9))
        cur.next = newnode
        cur = cur.next
    return head


def get_dll(n):
    """
    returns linkedlist of range n
    """
    if n<1:
        return None
    head = DoubleListNode(0)
    cur = head
    for i in range(1, n):
        newnode = DoubleListNode(i)
        cur.next = newnode
        newnode.prev = cur
        cur = cur.next
    return head

def print_ll(head):
    cur = head
    s = ""
    while cur:
        s += str(cur.val) + "->"
        cur = cur.next
    s+="None"
    print(s)



def get_random_ll(n):
    if n<1:
        return None
    head = RandomListNode(0)
    cur = head
    nodes = {}
    for i in range(n):
        cur.next = RandomListNode(randint(0, 10))
        nodes[i] = cur.next
        cur = cur.next

    cur = head.next
    for i in range(n):
        cur.random = nodes[randint(0, n-1)]
        cur = cur.next

    return head.next

def print_random_ll(head):
    while head:
        headrandomval = head.random.label if head.random else None
        print("val:{} random:{}".format(head.label, headrandomval))
        head = head.next

# print(levelOrder(a))
# print(dist(b, f.val, 0))