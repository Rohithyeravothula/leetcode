from graph import ListNode, get_ll, print_ll
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        def reverseList(head):
            if not head:
                return head
            p,c,n = None, head, head.next
            while c:
                c.next = p
                p = c
                c = n
                n = n.next if n else None
            return p
        
        def getMiddleNode(head):
            if not head or not head.next:
                return head
            fast = head
            slow = head
            prev = None
            while fast and fast.next:
                fast = fast.next.next
                prev = slow
                slow = slow.next
            return prev

        if head:
            midNode = getMiddleNode(head)
            l1 = head
            l2 = midNode.next
            midNode.next = None
            l2 = reverseList(l2)
            dh = ListNode(0)
            ch = dh
            while l2:
                if l1:
                    ch.next = l1
                    ch = ch.next
                    l1 = l1.next
                    ch.next = None
                ch.next = l2
                ch = ch.next
                l2 = l2.next
                ch.next = None



l1 = get_ll(6)
print_ll(l1)
s = Solution()
s.reorderList(l1)
print_ll(l1)





