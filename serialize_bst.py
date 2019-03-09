# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def build(cur):
            if not cur:
                return '#'
            return "{},{},{}".format(str(cur.val), build(cur.left), build(cur.right))
        return build(root)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def build(cur, i, l):
            if i>=l or cur[i] == '#':
                return None, i+1
            node = TreeNode(cur[i])
            node.left, li = build(cur, i+1, l)
            node.right, ri = build(cur, li, l)
            return node, ri 
        d = data.split(",")
        l = len(d)
        return build(d, 0, l)[0]

# Your Codec object will be instantiated and called as such:
from graph import leetcode_tree, TreeNode, inorder
t = leetcode_tree([1,2,3,4])
t = leetcode_tree([])
codec = Codec()
# print(codec.serialize(t))
nr = codec.deserialize(codec.serialize(t))
print(inorder(nr))