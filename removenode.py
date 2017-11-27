# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        s=head
        e=head
        c=0
        while c<n:
            c+=1
            s=s.next
        
        while s is not None and s.next is not None and e.next is not None:
            s=s.next
            e=e.next
        
        if e is None or e.next is None:
            return head
        elif e.next is not None and e.next.next is not None:
            e.next = e.next.next
        
        