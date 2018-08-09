class ALNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.arbitraty = None

def deepCopy(head):
    cur = head
    while cur:
        cur_copy = ALNode(-1*cur.val)
        cur_next = cur.next
        cur.next = cur_copy
        cur_copy.next = cur_next
        cur = cur_next

    cur = head
    cur_copy = cur.next
    while cur:
        if cur.arbitraty:
            cur_copy.arbitraty = cur.arbitraty.next
        cur = cur.next.next
        if cur:
            cur_copy = cur.next

    cur = head
    cur_copy = cur.next
    copy_head = cur_copy
    while cur:
        print("val: ", cur.val)
        cur.next = cur_copy.next
        if cur_copy.next:
            cur_copy.next = cur_copy.next.next
        cur = cur.next
        if cur:
            cur_copy = cur.next

    return copy_head

def print_list(head):
    cur = head
    while cur:
        if not cur.arbitraty:
            print(cur.val)
        else:
            print(cur.val, cur.arbitraty.val)
        cur = cur.next

a = ALNode(1)
b = ALNode(2)
c = ALNode(3)
d = ALNode(4)
a.next = b
a.arbitraty = b
b.next = c
b.arbitraty = d
c.next = d
c.arbitraty = a
d.arbitraty = a




print_list(a)
copy_head = deepCopy(a)
print_list(copy_head)
