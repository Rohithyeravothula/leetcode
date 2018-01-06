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
        def construct_serialization(cur):
            if cur is None:
                return "N"
            else:
                return  str(cur.val) + "," + construct_serialization(cur.left) + "," + construct_serialization(cur.right)
        return construct_serialization(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        if len(data) == 0 or data[0] == "N":
            return None

        def construct_tree(arr, index):
            if arr[index] == "N":
                return None, index+1
            else:
                cur = TreeNode(arr[index])
                cur.left, right_index = construct_tree(arr, index+1)
                cur.right, update_index = construct_tree(arr, right_index)
                return cur, update_index

        return construct_tree(data, 0)[0]

        


from graph import *

s=Codec()
# [1,2,3,None, None,4,5]
t = leetcode_tree([])
srz = s.serialize(t)
print(srz)
newt = s.deserialize(srz)
print(inorder(newt))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))