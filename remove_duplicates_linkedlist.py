# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur and cur.next and cur.next.val == head.val:
            cur = cur.next
        head = cur
        track = head
        cur = head.next
        while cur:
            cur_val = cur.val
            while cur and cur.next and cur.next.val == cur_val:
                cur = cur.next
            track.next = cur
            track = track.next
            cur = cur.next
        return head
            
            
        