# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head

        cur = head
        cur_next = head.next
        cur_next_next = cur_next.next
        reverse_list = self.swapPairs(cur_next_next)
        cur.next = reverse_list
        cur_next.next = cur
        return cur_next


from extras import *


l = get_list(1,9)
print_list(l)
s=Solution()
r = s.swapPairs(l)
print_list(r)

        


