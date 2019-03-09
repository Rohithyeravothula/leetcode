class Solution:
    def openLock(self, deadends, target: str) -> int:
        if target == "0000":
            return 0
        def get_children(val):
            children = []
            for i in range(4):
                p1 = str((int(val[i]) + 1)%10)
                p2 = str((int(val[i]) - 1)%10)
                children.append(val[:i] + p1 + val[i+1:])
                children.append(val[:i] + p2 + val[i+1:])
            return children
        seen = set()
        deadends = set(deadends)
        if "0000" in deadends or target in deadends: return -1
        cur = ["0000"]
        seen.add(cur[0])
        count = 1
        while cur:
            nxt = []
            for val in cur:
                for ch in get_children(val):
                    if ch == target:
                        return count
                    if ch not in seen and ch not in deadends:
                        nxt.append(ch)
                        seen.add(ch)
            cur = nxt
            count += 1
        return -1


deadends = ["0201","0101","0102","1212","2002"]
target = "0000"
print(Solution().openLock(deadends, target))
