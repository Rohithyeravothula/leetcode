# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self)

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        s1 = [root]
        s2 = []
        while len(s1) != 0 or len(s1) != 0:
            # print(s1, s2)
            cur = []
            while len(s1) != 0:
                p = s1.pop()
                cur.append(p)
                if p is not None:
                    s2.append(p.right)
                    s2.append(p.left)
            l = len(cur)
            for i in range(l-1, 0, -1):
                if cur[i] is not None:
                    cur[i].next = cur[i-1]
            cur = []
            while len(s2) != 0:
                p = s2.pop()
                cur.append(p)
                if p is not None:
                    s1.append(p.left)
                    s1.append(p.right)
            l = len(cur)
            for i in range(0, l-1):
                if cur[i] is not None:
                    cur[i].next = cur[i+1]
            # print(s1, s2)



a = TreeLinkNode(1)
a.left = TreeLinkNode(2)
a.right = TreeLinkNode(3)
a.right.left = TreeLinkNode(4)
a.right.right = TreeLinkNode(5)


s=Solution()
print(s.connect(a))
print(a.next, a.left.next, a.right.next, a.right.left.next, a.right.right.next)