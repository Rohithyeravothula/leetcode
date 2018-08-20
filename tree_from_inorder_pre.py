class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.pre_index = 0
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        def build(post_start, post_end):
            if post_start > post_end or self.pre_index >= l:
                return None
            ele = pre[self.pre_index]
            self.pre_index += 1
            post_pos = post_map[ele]
            cur_node = TreeNode(ele)
            cur_node.left = build(post_start, post_pos-1)
            cur_node.right = build(post_pos+1, post_end)
            return cur_node


        l = len(post)
        post_map = {}
        for i, v in enumerate(post):
            post_map[v] = i

        self.pre_index = 0
        ans = build(0, l-1)
        return ans

from graph import *


preorder = [1,2,3]
postorder = [2,3,1]
s = Solution()
t = s.constructFromPrePost(preorder, postorder)
# print(inorder(t))
print(t.val)
print(t.left.val)
print(t.right.val)


