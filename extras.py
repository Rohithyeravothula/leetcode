class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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
	print()

def get_list(s,e):
	assert s<=e
	test_list = ListNode(s)
	cur = test_list
	for i in range(s+1, e):
		cur.next = ListNode(i)
		cur = cur.next
	return test_list

# second_test_list = ListNode(10)
# second_test_list.next = test_list.next.next