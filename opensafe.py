from collections import deque
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        def get_children(s):
            children = []
            for i in range(0, 4):
                children.append(s[0:i]+ str((int(s[i])+1)%10) + s[i+1:])
                children.append(s[0:i]+ str((int(s[i])-1)%10) + s[i+1:])
            return children

        # return get_children("1111")
        if "0000" in deadends:
            return -1
        visited = {"0000"}
        for d in deadends:
            visited.add(d)
        queue = deque([("0000", 0)])
        while len(queue) != 0:
            # print(queue)
            # print()
            cur, level = queue.popleft()
            children = get_children(cur)
            for c in children:
                if c not in visited and c==target:
                    # print(c, level)
                    return level+1
                if c not in visited:
                    visited.add(c)
                    queue.append((c, level+1))
        return -1


s=Solution()
deadends = ["0000","0101","0102","1212","2002"]
target = "0202"
print(s.openLock(deadends, target))