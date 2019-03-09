class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def topo(n, a, pe, te, p):
            # print(n, a, pe, te)
            pe.add(n)
            for c in a[n]:
                if c in pe:
                    return False
                elif c not in te:
                    cp = topo(c, a, pe, te, p)
                    if not cp:
                        return False
            pe.remove(n)
            te.add(n)
            p.append(n)
            return True

        degree = [0]*numCourses
        adl = [[] for _ in range(numCourses)]
        for i, j in prerequisites:
            degree[j] += 1
            adl[i].append(j)
        PE = set()
        TE = set()
        ans = []
        for node, deg in enumerate(degree):
            if deg == 0:
                path = []
                if not topo(node, adl, PE, TE, path):
                    return []
                ans.extend(path)
        if len(ans) == numCourses:
            return ans
        return []


nc, pre = 0, []
nc, pre = 2, [[1,0]]
nc, pre = 4, [[1,0],[2,0],[3,1],[3,2]]
nc, pre = 8,[[1,0],[2,6],[1,7],[5,1],[6,4],[7,0],[0,5]]
print(Solution().canFinish(nc, pre))