# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import math
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def length(cur):
            c=0
            while cur is not None:
                cur = cur.next
                c+=1
            return c

        l1 = length(headA)
        l2 = length(headB)
        longer = headB
        shorter = headA
        if l1>l2:
            longer = headA
            shorter  = headB

        start = abs(l1-l2)
        while start:
            longer = longer.next
            start -= 1

        while shorter is not None and longer is not None:
            if longer == shorter:
                return longer
            longer = longer.next
            shorter = shorter.next
        return None

from extras import *
s=Solution()
print(s.getIntersectionNode(test_list, second_test_list).val)