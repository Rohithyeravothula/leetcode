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
                return ['X']
            return [str(cur.val)] + build(cur.left) + build(cur.right)
        return "@".join(build(root))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = data.split("@")
        self.index = 0
        def build(values):
            if values[self.index] == "X":
                self.index += 1
                return None
            cur = TreeNode(int(values[self.index]))
            self.index += 1
            cur.left = build(values)
            cur.right = build(values)
            return cur
        return build(values)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))