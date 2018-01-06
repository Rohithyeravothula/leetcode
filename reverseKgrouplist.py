# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse(self, head):
        prev = None
        cur = head
        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt
        return prev

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k==1:
            return head

        if head is None or head.next is None:
            return head

        cur = head
        c = 1
        while cur.next is not None and c<k:
            cur = cur.next
            c+=1

        if c!=k:
            return head

        nxt = cur.next
        cur.next = None
        reverse_head = self.reverse(head)
        reverse_list = self.reverseKGroup(nxt, k)
        head.next = reverse_list
        return reverse_head

from extras import *


l = get_list(0,0)
print_list(l)
s=Solution()
r = s.reverseKGroup(l, 100)
print_list(r)

        


