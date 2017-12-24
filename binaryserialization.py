# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from graph import *

class Codec:
    def get_inorder(self, root):
        a=[]
        def __inorder(cur):
            if cur is None:
                return None
            __inorder(cur.left)
            a.append(cur.val)
            __inorder(cur.right)
        __inorder(root)
        return a


    def get_preorder(self, root):
        a=[]
        def __preorder(cur):
            if cur is None:
                return None
            a.append(cur.val)
            __preorder(cur.left)
            __preorder(cur.right)
        __preorder(root)
        return a

    def construct(self, inorder, preorder):
        l = len(inorder)
        inomap = {}
        for idx, val in enumerate(inorder):
            inomap[val] = idx
        self.index = 0
        def __construct(pre, left, right):
            if left == right:
                return None
            elif left == right-1:
                self.index += 1
                return TreeNode(inorder[left])
            else:
                idx = inomap[pre[self.index]]
                cur = TreeNode(pre[self.index])
                self.index += 1
                cur.left = __construct(pre, left, idx)
                cur.right = __construct(pre, idx+1, right)
                return cur
        return __construct(preorder, 0, l)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return None
        ino = self.get_inorder(root)
        pre = self.get_preorder(root)
        inos = ",".join(list(map(lambda x: str(x), ino)))
        pres = ",".join(list(map(lambda x: str(x), pre)))
        return "{}\n{}".format(inos, pres)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data is None:
            return None
        inos, pres = data.split("\n")
        ino = list(map(lambda x: int(x), inos.split(",")))
        pres = list(map(lambda x: int(x), pres.split(",")))
        return self.construct(ino, pres)
        

t=leetcode_tree([])
s=Codec()
print(s.get_inorder(t))
print(s.get_preorder(t))
print(inorder(s.construct(s.get_inorder(t), s.get_preorder(t))))
print(s.serialize(t))
print(s.get_inorder(s.deserialize(s.serialize(t))))