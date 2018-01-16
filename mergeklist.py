# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
    	return str(self.val)

    def __repr__(self):
    	return str(self)

from heapq import heappush, heappop
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        result = ListNode(0)
        curresult = result
        kheap = []
        k = len(lists)
        for i in range(0, k):
        	if lists[i] is not None:
        		heappush(kheap, (lists[i].val, i, lists[i]))
        		lists[i] = lists[i].next
        while kheap:
        	# print(kheap)
        	(nodeval, index, node) = heappop(kheap)
        	curresult.next = node
        	node.next = None
        	curresult = curresult.next
        	if lists[index] is not None:
        		heappush(kheap, (lists[index].val, index, lists[index]))
        		lists[index] = lists[index].next
        return result.next



from extras import *
t1 = list_to_linkedlist([1,1,2])
t2 = list_to_linkedlist([1,2,2])
lst = [t1,t2]
s=Solution()
ls = s.mergeKLists(lst)
while ls:
	print(ls)
	ls = ls.next