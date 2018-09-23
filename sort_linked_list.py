# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from heapq import heappush, heappop, heapify

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = [(node.val, index, node) for index, node in enumerate(lists) if node]
        heapify(h)
        sorted_head = ListNode(-1)
        cur = sorted_head
        while h:
        	(cur_min, index, node) = heappop(h)
        	next_node = node.next
        	if next_node:
        		heappush(h, (next_node.val,index, next_node))
        	node.next = None
        	cur.next = node
        	cur = cur.next
        return sorted_head.next


from graph import *
l1 = get_ll(4)
l2 = get_ll(7)
inp = [l1, l2]
s = Solution()
print_ll(s.mergeKLists(inp))


        