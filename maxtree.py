class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorder(root, a):
    if root is None:
        return None
    inorder(root.left, a)
    a.append(root.val)
    inorder(root.right, a)


class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def tree(a, i, j):
            if i==j:
                return TreeNode(a[i])
            elif i>j:
                return None
            else:
                m=a[i]
                mi = i
                for r in range(i, j+1):
                    if m<a[r]:
                        m=a[r]
                        mi = r
                cur = TreeNode(a[mi])
                cur.left = tree(a, i, mi-1)
                cur.right = tree(a, mi+1, j)
                return cur
        return tree(nums, 0, len(nums)-1)
            
arr = [1]
s=Solution()
t = s.constructMaximumBinaryTree(arr)
a = []
inorder(t, a)
print(a)