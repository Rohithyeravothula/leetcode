def insertionSortList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
        return head
    start = head
    tail = head
    tailnext = tail.next
    count = 0
    while tailnext and count < 10:
        count += 1
        # print(tailnext.val)
        if tailnext.val < start.val:
            tail.next = tailnext.next
            tailnext.next = start
            start = tailnext
            tailnext = tail.next
        elif tailnext.val >= tail.val:
            tail = tail.next
            tailnext = tailnext.next
        else:
            cur = start
            while cur.next.val < tailnext.val:
                cur = cur.next
            tail.next = tailnext.next
            tailnext.next = cur.next
            cur.next = tailnext
            tailnext = tail.next

    return start

from graph import *
# l = ListNode(5)
# l.next = ListNode(8)
# l.next.next = ListNode(13)
# l.next.next.next = ListNode(8)
# l.next.next.next.next = ListNode(9)
l = get_rand_ll(20)
print_ll(l)
nl = insertionSortList(l)
print_ll(nl)