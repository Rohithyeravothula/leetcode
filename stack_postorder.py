from graph import leetcode_tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, head):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        cur = head 
        stk = []
        ans = []
        while stk or cur:
        	# print(stk, cur)
        	while cur:
        		stk.append(cur)
        		cur = cur.left
        	ans.append(stk.pop())
        	while stk:
        		print(stk)
        		top = stk[-1]
        		if top.right:
        			cur = top.right
        		else:
        			ans.append(stk.pop())
        return ans

s = Solution()
t = leetcode_tree([1,2,3,4,5])
print(s.postorderTraversal(t))
