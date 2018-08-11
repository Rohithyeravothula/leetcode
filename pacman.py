class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        def get_next_moves(x,y):
            ans = []
            if x>self.xminlimit+ 1:
                ans.append((x-1, y))
            if y>self.yminlimit+ 1:
                ans.append((x, y-1))
            if x<self.xlimit-1:
                ans.append((x+1, y))
            if y<self.ylimit-1:
                ans.append((x, y+1))
            return ans

        self.xminlimit = 0
        self.yminlimit = 0
        self.xlimit = target[0]
        self.ylimit = target[1]

        ghost_locations = set()
        for g in ghosts:
            ghost_locations.add((g[0], g[1]))
            self.xlimit = max(self.xlimit, g[0])
            self.xminlimit = min(self.xminlimit, g[0])
            self.ylimit = max(self.ylimit, g[1])
            self.yminlimit = min(self.yminlimit, g[1])
        locations = [(0, 0)]
        iter_count = 0
        while locations and iter_count < 10000:
            new_ghosts = set()
            for loc in ghost_locations:
                children = get_next_moves(loc[0], loc[1])
                for c in children:
                    new_ghosts.add(c)
            ghost_locations = new_ghosts
            iter_count += 1
            cur = locations.pop() 
            children = get_next_moves(cur[0], cur[1])
            for child in children:
                if child not in ghost_locations:
                    if child[0] == target[0] and child[1] == target[1]:
                        return True
                    locations.append(child)
            # print(locations, ghost_locations)
        return False

ghs = [[1,8],[-9,0],[-7,-6],[4,3],[1,3]]
tg = [6,-9]
s=Solution()
print(s.escapeGhosts(ghs, tg))

