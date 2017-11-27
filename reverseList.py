
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        
        def reverse(cur, count, m,n):
            if cur is None or cur.next is None:
                return cur, None

            elif count == n:
                return cur, cur.next

            elif count >= m and count < n:
                nxt = cur.next
                cur.next = None
                head, head_nxt = reverse(nxt, count+1, m, n)
                if count == m:
                    cur.next = head_nxt
                    nxt.next = cur
                else:
                    nxt.next = cur
                return head, head_nxt
            else:
                head, head_nxt=reverse(cur.next, count+1, m, n)
                if count == m-1:
                    cur.next=head
                return head, head_nxt
        newhead, _  = reverse(head, 1, m, n)
        if m == 1:
            return newhead
        else:
            return head


def printList(a):
    s=""
    while a is not None:
        s+=str(a.val)+"->"
        a=a.next
    print(s)
   

def get_list(n):
    if n == 0:
        return ListNode(0)
    start = ListNode(-1)
    n=int(str(n)[::-1])
    cur = start
    while n>0:
        cur.next = ListNode(int(n%10))
        n=int(n/10)
        cur = cur.next  
    return start.next

a=1
a=get_list(a)
s=Solution()
printList(a)
c=s.reverseBetween(a,1,1)
printList(c)
