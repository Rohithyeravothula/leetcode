# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return head
        cur = head
        while cur is not None:
            new = RandomListNode(cur.label)
            nxt = cur.next
            new.next = cur.next
            cur.next = new
            cur = cur.next.next
        cur = head
        while cur is not None:
            if cur.random is not None:
                cur.next.random = cur.random.next
            cur = cur.next.next
        cur = head
        lst = head.next
        while cur.next is not None:
            nxt = cur.next
            cur.next = cur.next.next
            cur = nxt
        return lst

def printList(root):
    cur = root
    while cur is not None:
        print(cur.label, cur.random.label)
        cur = cur.next
        


a=RandomListNode(1)
a.next = RandomListNode(2)
a.next.next= RandomListNode(3)
a.random = a.next.next
a.next.random = a.next.next
a.next.next.random = a.next
# printList(a)
s=Solution()
ans = s.copyRandomList(a)