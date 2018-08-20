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
        def build(post_start, post_end, l):
            # print(post_start, post_end, self.pre_index, pre[self.pre_index], post_map[pre[1+self.pre_index]])
            if post_start > post_end or self.pre_index >= l:
                return None

            ele = pre[self.pre_index]
            cur_root = TreeNode(ele)
            self.pre_index+=1
            if post_start == post_end or self.pre_index >= l:
                return cur_root
            left_root = pre[self.pre_index]
            post_pos = post_map[left_root]
            cur_root.left = build(post_start, post_pos, l)
            cur_root.right = build(post_pos+1, post_end-1, l)
            return cur_root


        l = len(post)
        post_map = {}
        for i, v in enumerate(post):
            post_map[v] = i

        self.pre_index = 0
        ans = build(0, l-1, l)
        return ans

from graph import *

# preorder =[1, 2, 4, 8, 9, 5, 3, 6, 7]
# postorder = [8, 9, 4, 5, 2, 6, 7, 3, 1 ]
# preorder = [1,2,4,5,3,6,7]
# postorder = [4,5,2,6,7,3,1]
preorder = [1,2,3]
postorder = [2,3,1]
s = Solution()
t = s.constructFromPrePost(preorder, postorder)
print(inorder(t))
