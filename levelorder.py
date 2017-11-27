
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self)

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        s1 = [root]
        s2 = []
        ans = []
        while len(s1) != 0 or len(s2)!=0:
            # print(s1, s2, ans)
            i_ans = []
            while len(s1)!=0:
                p = s1.pop()
                if p is not None:
                    s2.append(p.right)
                    s2.append(p.left)
                    i_ans.append(p.val)
            if len(i_ans) != 0:
                i_ans = i_ans[::-1]
                ans.append(i_ans)
            i_ans = []
            # print(s1, s2, ans)
            while len(s2)!=0:
                p = s2.pop()
                if p is not None:
                    s1.append(p.left)
                    s1.append(p.right)
                    i_ans.append(p.val)
            if len(i_ans) != 0:
                ans.append(i_ans)
            # print(s1, s2, ans)
        return ans

a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.left = TreeNode(4)
a.right.right = TreeNode(5)


s=Solution()
print(s.levelOrder(a))