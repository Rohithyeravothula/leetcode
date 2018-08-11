class Solution:
    def findCircleNum(self, adj):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def get_friends(m, i, n):
            children = []
            for j in range(0, n):
                if m[i][j] == 1 and i!=j:
                    children.append(j)
            return children
        visited = set()
        l = len(adj)
        circles = 0
        for node in range(l):
            if node in visited:
                continue
            cur = [node]
            while cur:
                newcur = []
                for curnode in cur:
                    friends = get_friends(adj, curnode, l)
                    for frd in friends:
                        if frd not in visited:
                            newcur.append(frd)
                    visited.add(curnode)
                cur = newcur
            circles += 1
            visited.add(node)
        return circles


amd = []
s = Solution()
print(s.findCircleNum(amd))