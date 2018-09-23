# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return sort_list(head)

def break_two(head):
    if not head:
        return None, None
    if head and head.next and not head.next.next:
        shead = head.next
        head.next = None
        return head, shead
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next 
        slow = slow.next
    shead = slow.next
    slow.next = None
    return head, shead

def merge_lists(l1, l2):
    nl = ListNode(0)
    cur = nl
    while l1 or l2:
        if l2 and not l1:
            l1, l2 = l2, l1

        if l1 and not l2:
            node = l1
            l1 = l1.next
            node.next = None
            cur.next = node
            cur = cur.next
        else:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            node = l1
            l1 = l1.next
            node.next = None
            cur.next = node
            cur = cur.next
    return nl.next


def sort_list(head):
    if not head or not head.next:
        return head

    first, second = break_two(head)
    first_sort = sort_list(first)
    second_sort = sort_list(second)
    newhead = merge_lists(first_sort, second_sort)
    return newhead





from graph import *
# l1 = get_rand_sorted_ll(1)
# l2 = get_rand_sorted_ll(2)
# print_ll(l1)
# print_ll(l2)
# nl = merge_lists(l1, l2)
# print_ll(nl)
# h1, h2 = break_two(l1)
# print_ll(h1)
# print_ll(h2)

l1 = get_rand_ll(10)
print_ll(l1)
nl = Solution().sortList(l1)
print_ll(nl)