class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        def find(a, i):
            if a[i] == -1:
                return i
            return find(a, a[i])

        def union(a, i, j):
            rooti = find(a, i)
            rootj = find(a, j)
            if rooti != rootj:
                a[rooti] = rootj

        def check(a, i, j):
            rooti = find(a, i)
            rootj = find(a, j)
            return rooti == rootj
        mapper = {chr(i+96):i for i in range(1, 27)}
        a = [-1]*27
        unequals = []
        for eq in equations:
            x,y = eq[0], eq[-1]
            if eq[1] == "=":
                union(a, mapper[x], mapper[y])
            else:
                unequals.append((x,y))
        for (x,y) in unequals:
            if x==y or check(a, mapper[x], mapper[y]):
                return False
        return True

inp = ["b==a","a==c", "a!=a"]
inp = ["a!=a"]
inp = ["a==b","b!=a"]
inp = ["g==c","f!=e","e==b","j==b","g!=a","e==c","b!=f","d!=a","j==g","f!=i","a==e"]
inp = ["a==b","b==c","a==c"]
inp = ["a==b","b!=c","c==a"]
inp = ["b==a", "a==c", "c!=d"]
inp = ["b==a","a==b"]
inp = ["c==c","b==d","x!=z"]
inp = []
print(Solution().equationsPossible(inp))