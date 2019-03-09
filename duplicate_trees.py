
from collections import defaultdict

class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        def build(cur, seen):
            if not cur:
                return '#'
            key = str(cur.val) + build(cur.left, seen) + build(cur.right, seen)
            seen[key].append(cur)
            return key
        seen = defaultdict(list)
        build(root, seen)
        return [val[0] for val in seen.values() if len(val) > 1]

from graph import leetcode_tree
t = leetcode_tree([0,0,0,0,None,None,0,None,None,None,0])
Solution().findDuplicateSubtrees(t)