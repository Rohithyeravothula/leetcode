# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val < l2.val:
            prev=l1
            cur = l1.next
            bottom = l2
            head = l1
        else:
            prev=l2
            cur=l2.next
            bottom=l1
            head=l2

        while cur is not None and bottom is not None:
            if cur.val < bottom.val:
                prev = cur
                cur = cur.next
            else:
                node = bottom
                bottom = bottom.next
                node.next= None
                prev.next = node
                node.next=cur
                prev=node

        if bottom is not None:
            prev.next = bottom

        return head

from extras import *

l1 = get_list(1,4)
l2 = get_list(2,5)
s=Solution()
l3 = s.mergeTwoLists(l1, l2)
print_list(l3)