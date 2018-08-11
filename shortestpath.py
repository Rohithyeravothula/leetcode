class Solution:
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        def path_count(cur, visited):
            visited.add(cur)
            path_lengths = []
            for child in graph[cur]:
                if child not in visited:
                    path_lengths.append(path_count(child, visited))
            if path_lengths == []:
                return 0
            if len(path_lengths) == 1:
                return 1+path_lengths[0]*2
            path_max = max(path_lengths)
            s = sum(path_lengths)*2 + 2*len(path_lengths) - 1
            return s-path_max

        min_dist = float("inf")
        for i in range(len(graph)):
            visited = set()
            path_length = path_count(i, visited)
            print(i, path_length)
            min_dist = min(min_dist, path_length)
        return min_dist

info = [[1],[0,2,4],[1,3,4],[2],[1,2]]
s = Solution()
print(s.shortestPathLength(info))




