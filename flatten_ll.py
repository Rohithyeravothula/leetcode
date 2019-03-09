class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        def flat(head):
            if not head:
                return head
            cur = head
            while cur:
                print(cur.val)
                curnext = cur.next
                if cur.child:
                    childtail = flat(cur.child)
                    cur.child = None
                    if not curnext:
                        cur.next = childtail
                        childtail.next = cur
                    else:
                        cur.next = cur.child 
                        cur.child.prev = cur
                        childtail.next = curnext
                        curnext.prev = childtail 
                    
                cur = curnext
            cur = head
            while cur.next:
                cur = cur.next
            return cur
        flat(head)
        return head



