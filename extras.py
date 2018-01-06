import random
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
    	if self is not None:
    		return str(self.val)
    	return "None"

    def __repr__(self):
    	return str(self)

def list_to_linkedlist(a):
	head = ListNode(a[0])
	start = head
	for i in a[1:]:
		start.next = ListNode(i)
		start = start.next
	return head

def print_2d_array(a):
	for i in a:
		print(i)

def print_list(a):
	while a is not None:
		print(a.val, end="->")
		a=a.next
	print("None")

def get_list(e,s=0):
	if s==e:
		return None
	test_list = ListNode(s)
	cur = test_list
	for i in range(s+1, e):
		cur.next = ListNode(i)
		cur = cur.next
	return test_list


def create_list(r):
	assert(r > 1)
	head = ListNode(1)
	cur = head
	for i in range(2, r):
		cur.next = ListNode(i)
		cur = cur.next
	return head

def create_random_list(r, left = 1, right=10, sort_flag=False):
	if r<1:
		return None
	nodes = [random.randint(left, right) for _ in range(0, r)]
	if sort_flag:
		nodes.sort()
	print(nodes)
	head = ListNode(nodes[0])
	cur = head
	for i in nodes[1:]:
		cur.next = ListNode(i)
		cur = cur.next
	return head



# second_test_list = ListNode(10)
# second_test_list.next = test_list.next.next