from pprint import pprint
class Solution:
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        l = len(quiet)
        adj = [[0]*l for _ in range(l)]
        for i,j in richer:
            adj[j][i] = 1

        pprint(adj)

        def get_rich_children(i):
            children = []
            for j in range(l):
                if adj[i][j] == 1:
                    children.append(j)
            return children

        def get_quiteness(cur, max_quiet):
            print(cur, quiet[cur], max_quiet)
            if max_quiet[cur] != -1:
                return max_quiet[cur]
            cur_max = float("inf")
            cur_per = None
            children = get_rich_children(cur)
            for child in children:
                next_per, next_max = get_quiteness(child, max_quiet)
                if next_max < cur_max:
                    cur_max = next_max
                    cur_per = next_per


            if cur_per is None:
                cur_max = quiet[cur]
                cur_per = cur
            max_quiet[cur] = (cur_per, cur_max)
            return max_quiet[cur]

        ans = [-1]*l
        for i in range(l):
            get_quiteness(i, ans)
            # break
        quiet_persons = [p for p,_ in ans]
        return quiet_persons


richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]
# richer = []
# quiet = []
# richer = [[0,1]]
# quiet = [15,9]
s = Solution()
print(s.loudAndRich(richer, quiet))


[5,5,2,5,4,5,6,5]
[5,5,2,5,4,5,6,7]