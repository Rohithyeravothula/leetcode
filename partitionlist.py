# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less = ListNode(1) # placeholder
        rest = ListNode(1) # placeholder
        cur_less = less
        cur_rest = rest
        cur = head
        while cur is not None:
            nxt = cur.next
            if cur.val < x:
                cur_less.next = cur
                cur.next = None
                cur_less = cur
            else:
                cur_rest.next = cur
                cur.next = None
                cur_rest = cur  
            cur.next = None
            cur = nxt
        rest = rest.next
        cur_less.next = rest
        return less.next

from extras import *
s=Solution()
l = create_random_list(10)
print_list(l)
r = s.partition(l, 4)
print_list(r)

