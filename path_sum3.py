from collections import defaultdict
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def build(cur, seen):
        	if not cur:
        		return
        	# print(cur.val, seen)
        	if cur.val in seen:
        		self.count += seen[cur.val]
        	if cur.val == sum:
        		self.count += 1
        	cursum = sum - cur.val
        	newseen = defaultdict(int)
        	for key, val in seen.items():
        		newseen[key - cur.val] = val
        	newseen[cursum] += 1
        	build(cur.left, newseen)
        	build(cur.right, newseen)
        self.count = 0
        build(root, {})
        return self.count

from graph import leetcode_tree
null = None
t = leetcode_tree([10,5,-3,3,2,null,11,3,-2,null,1])
print(Solution().pathSum(t, 17))