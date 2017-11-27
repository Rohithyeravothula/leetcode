# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        if head.next.next is None:
            if head.next.val == head.val:
                return True
            return False
        def reverse(head):
            if head is None or head.next is None:
                return head
            prev = head
            cur = head.next
            nxt = head.next.next
            prev.next = None
            while cur is not None:
                cur.next = prev
                prev = cur
                cur = nxt
                if nxt is None:
                    break
                nxt = nxt.next
            return prev

        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            if fast.next.next is None:
                fast = None
            else:
                fast = fast.next.next
            slow = slow.next
        
        slowNxt = slow.next
        slow.next = None
        fast = head

        ans = True
        # print(fast.val, slow.val)
        rev = reverse(slowNxt)

        slow = rev
        printList(fast)
        printList(slow)
        while fast is not None and slow is not None:
            if fast.val != slow.val:
                ans = False
                break
            fast = fast.next
            slow = slow.next
        return ans





def printList(a):
    s=""
    while a is not None:
        s+=str(a.val)+"->"
        a=a.next
    print(s)
   

# def get_list(n):
#     if n == 0:
#         return ListNode(0)
#     start = ListNode(-1)
#     n=int(str(n)[::-1])
#     cur = start
#     while n>0:
#         cur.next = ListNode(int(n%10))
#         n=int(n/10)
#         cur = cur.next  
#     return start.next

def get_list(n):
    start = ListNode(n[0])
    cur = start
    l = len(n)
    count = 1
    while count<l:
        cur.next=ListNode(n[count])
        cur = cur.next
        count += 1
    return start
        
a="1211"
a=get_list(a)
# printList(a)
s=Solution()
print(s.isPalindrome(a))