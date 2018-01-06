class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left = [root]
        right = []
        averages = []
        while left or right:
            ans = []
            while left:
                cur = left.pop()
                if cur is not None:
                    right.append(cur.left)
                    right.append(cur.right)
                    ans.append(cur.val)
            if len(ans)!=0:
                averages.append(sum(ans)/len(ans))
            ans = []
            while right:
                cur = right.pop()
                if cur is not None:
                    left.append(cur.right)
                    left.append(cur.left)
                    ans.append(cur.val)
            if len(ans)!=0:
                averages.append(sum(ans)/len(ans))
        return averages
