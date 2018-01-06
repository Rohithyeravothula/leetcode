# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is not None and head.next is not None:

            def reverse(head):
                prev = None
                cur = head
                while cur is not None:
                    nxt = cur.next
                    cur.next = prev
                    prev = cur
                    cur = nxt
                return prev

            l = 0
            cur = head
            while cur is not None:
                cur = cur.next
                l+=1

            c=1
            k = l//2
            cur = head
            while c<k:
                cur = cur.next 
                c+=1

            left = head
            right = reverse(cur.next)
            merge = ListNode(1)
            cur_merge = merge
            while left is not None or right is not None:
                if left is not None:
                    next_left = left.next
                    cur_merge.next = left
                    left.next = None
                    cur_merge = left
                    left = next_left

                if right is not None:
                    next_right = right.next
                    cur_merge.next = right
                    right.next = None
                    cur_merge = right
                    right = next_right



from extras import *
l = get_list(0)
print_list(l)
s=Solution()
r=s.reorderList(l)
print_list(l)

# left = ListNode(1)
# right = ListNode(1)
# cur_left=left
# cur_right = right
# cur = head
# while cur is not None:
#   nxt = cur.next
#   cur_left.next = cur
#   cur.next = None
#   cur_left = cur

#   if nxt is not None:
#       cur = nxt
#       nxt = cur.next
#       cur_right.next  = cur 
#       cur.next = None
#       cur_right = cur
#       cur = nxt.next
#   else:
#       break