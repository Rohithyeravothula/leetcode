class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        l = len(rooms)
        if l == 0:
        	return 0
        cur_keys = set(rooms[0])
        visited = set([0])
        while cur_keys:
        	current = cur_keys.pop()
        	if current not in visited and current < l:
        		cur_keys = cur_keys.union(rooms[current])
        		visited.add(current)
        if len(visited) == l:
        	return True
        return False




# rinfo = [[1,2,3]]
rinfo = [[1,3],[3,0,1],[2],[0]]
# rinfo = [[1],[2],[3],[]]
s = Solution()
print(s.canVisitAllRooms(rinfo))