from graph import leetcode_tree

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        cur = root
        stk = []
        ans = []
        while cur or stk:
            # print(cur, stk)
            while cur:
                stk.append(cur)
                cur = cur.left
            while stk:
                top = stk.pop()
                ans.append(top)
                if top.right:
                    cur = top.right
                    break
        return ans

s = Solution()
t = leetcode_tree([])
# print(t.val)
print(s.inorderTraversal(t))