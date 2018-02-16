class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        l = len(start)
        def ch(a,b):
            a = list(a)
            b = list(b)
            a.sort()
            b.sort()
            return a==b
        def get_children(a):
            ans = []
            nodes = list(a)
            pos = []
            for i in range(0, l-1):
                if a[i:i+2] in {"XL", "RX"}:
                    pos.append(i)
            for i in pos:
                nodes[i], nodes[i+1] = nodes[i+1],nodes[i]
                # print(i, "".join(nodes))
                ans.append(nodes[:])
                nodes[i], nodes[i+1] = nodes[i+1],nodes[i]
            return list(map(lambda x: "".join(x), ans))

        if start == end:
            return True
        elif len(start) != len(end):
            return False
        elif not ch(start, end):
            return False
        stk = [start]
        visited = set()
        while stk:
            # print(stk)
            print(len(visited))
            cur = []
            for i in stk:
                children = get_children(i)
                for child in children:
                    if child == end:
                        return True
                    elif child not in visited:
                        visited.add(child)
                        cur.append(child)
            stk = cur
        return False

a="XXXLXXLXXLXXRXXXRXLXRXRXXXXXLX"
b="LLLXXXXXXXXXXXXXRRLXXXXXXXRRLX"
s=Solution()
print(s.canTransform(a,b))
