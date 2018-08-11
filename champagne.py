import math


class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """

        def get_parents(x, y):
            if y==0:
                return [(x-1, y)]
            if y==x:
                return [(x-1, y-1)]
            return [(x-1, y), (x-1, y-1)]

        def get_val(total, i, j):
            if i == 0:
                return total
            if (i, j) in seen:
                return seen[(i, j)]
            cur =  0
            # print(i, j, get_parents(i, j))
            for (pi, pj) in get_parents(i, j):
                cur += max((get_val(total, pi, pj)-1)/2, 0)
            # print(cur)
            seen[(i,j)] = cur
            return cur

        seen = {}
        return min(get_val(poured, query_row, query_glass), 1)

prd = 100
qr = 85
qg = 39
s=Solution()
print(s.champagneTower(prd, qr, qg))

