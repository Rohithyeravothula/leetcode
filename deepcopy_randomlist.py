# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def newcopy(self, head):
        seen = {}
        cur = head
        chead = RandomListNode(0)
        newcur = chead
        while cur:
            node = RandomListNode(cur.label)
            seen[cur] = node
            newcur.next = node
            newcur = newcur.next
            cur = cur.next
        cur = head
        newcur = chead.next
        while cur:
            newcur.random = seen[cur.random] if cur.random else None
            newcur = newcur.next
            cur = cur.next
        return chead.next

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return head
        if not head.next:
            r = RandomListNode(head.label)
            if head.random:
                r.random = r
            return r
        cur = head
        
        while cur:
            newnode = RandomListNode(cur.label)
            curnext = cur.next
            cur.next = newnode
            newnode.next = curnext
            cur = newnode.next

        cur = head
        while cur:
            newcur = cur.next
            if cur.random:
                newcur.random = cur.random.next
            cur = newcur.next


        
        chead = head.next
        cur = head
        newcur = chead
        while newcur:            
            cur.next = newcur.next
            
            if newcur.next:
                newcur.next = newcur.next.next
            else:
                newcur.next = None
            
            cur = cur.next
            newcur = newcur.next

        return chead

s = Solution()
from graph import *
l = get_random_ll(4)
print_random_ll(l)
c = s.newcopy(l)
print_random_ll(c)
