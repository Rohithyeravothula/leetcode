from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root:
            return []
        seen = defaultdict(list)
        cur = [(root, 0, 0)]
        while cur:
            nxt = []
            for (node, x, y) in cur:
                seen[x].append((-y, node.val))
                if node.left:
                    nxt.append((node.left, x-1, y-1))
                if node.right:
                    nxt.append((node.right, x+1, y-1))
            cur = nxt

        # print(seen)
        for val in seen.values():
            val.sort()
        result = []
        for key, val in seen.items():
            valup = [v for _, v in val]
            result.append((key, valup))
        result.sort()
        return [val[1] for val in result]

from graph import leetcode_tree
t = leetcode_tree([1,2,3,4,5,6,7, None, None, 8, 9, None, None, 10, None])
t = leetcode_tree([0,2,1,3,None,None,None,4,5,None,7,6,None,10,8,11,9])
t = leetcode_tree([1,2,3,4,5,6,7])
t = leetcode_tree([3,9,20,None,None,15,7])
print(Solution().verticalTraversal(t))