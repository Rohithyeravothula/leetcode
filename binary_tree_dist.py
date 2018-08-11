# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[TreeNode]
        """
        if not root:
            return []
        def get_parents(cur):
            if cur:
                distances[cur.val] = -1
                if cur.left:
                    parents[cur.left.val] = cur.val
                    get_parents(cur.left)
                if cur.right:
                    parents[cur.right.val] = cur.val
                    get_parents(cur.right)
        parents = {}
        distances = {}
        get_parents(root)
        # print(parents)
        distances[target.val] = 0
        root_node = root.val
        cur_node = target.val
        while cur_node != root_node:
            cur_parent = parents[cur_node]
            distances[cur_parent] = distances[cur_node]+1
            cur_node = cur_parent

        def get_distances(cur):
            if cur:
                if cur.left and distances[cur.left.val] == -1:
                    distances[cur.left.val] = distances[cur.val]+1
                if cur.right and distances[cur.right.val] == -1:
                    distances[cur.right.val] = distances[cur.val]+1
                get_distances(cur.left)
                get_distances(cur.right)
        get_distances(root)
        # print(distances)
        ans = []
        for val, dist in distances.items():
            if dist == K:
                ans.append(val)
        return ans




from graph import leetcode_tree, TreeNode
t1 = [3,5,1,6,2,0,8,None,None,7,4]
t2 = []
t = leetcode_tree(t2)
s = Solution()
print(s.distanceK(t, TreeNode(5), 10))
