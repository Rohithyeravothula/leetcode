# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def add(left, right):
            ans = ListNode(-1)
            cur = ans
            carry = 0
            while left is not None and right is not None:
                s = left.val + right.val + carry
                carry = int(s/10)
                cur.next = ListNode(s%10)
                cur = cur.next
                left = left.next
                right = right.next

            while left is not None:
                s = left.val + carry
                carry = int(s/10)
                cur.next = ListNode(s%10)
                cur = cur.next
                left = left.next

            while right is not None:
                s = right.val + carry
                carry = int(s/10)
                cur.next = ListNode(s%10)
                cur = cur.next
                right = right.next

            if carry == 1:
                cur.next = ListNode(carry)

            return ans.next


        def reverse(head):
            if head is None or head.next is None:
                return head
            else:
                nxt = head.next
                head.next = None
                r = reverse(nxt)
                nxt.next = head
                return r

        n1 = reverse(l1)
        n2 = reverse(l2)
        # printList(n1)
        n3 = add(n1, n2)
        return reverse(n3)


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

a=10982734
b=164312937401376
a=get_list(a)
b=get_list(b)
printList(a)
printList(b)
s=Solution()
c=s.addTwoNumbers(a,b)
printList(c)