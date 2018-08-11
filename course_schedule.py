class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adjlist = [[] for _ in range(numCourses)]
        for i,j in prerequisites:
            adjlist[i].append(j)

        def dfs(cur, visited, path):
            for node in adjlist[cur]:
                if node in path:
                    return False
                elif node not in visited:
                    path.add(node)
                    if not dfs(node, visited, path):
                        return False
                    path.remove(node)
                    visited.add(node)
            visited.add(cur)
            return True

        visited = set()
        for i in range(numCourses):
            if i not in visited and not dfs(i, visited, set()):
                return False
            visited.add(i)
        return True




numc = 6
listofcourses = [[1,0],[0,1]]
s = Solution()
print(s.canFinish(numc, listofcourses))