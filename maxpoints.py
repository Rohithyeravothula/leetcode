def toPoint(a):
    return [Point(x,y) for x,y in a]


class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)


from collections import defaultdict
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        def gcd(x,y):
            if x==0 or y==0:
                return x+y
            if x>y:
                x,y = y,x
            return gcd(x, y%x)

        ans = 0
        for index, point in enumerate(points):
            cur = defaultdict(int)
            cur['a'] = 0
            same = 1
            vertical = 0
            for second_point in points[index+1:]:
                if second_point.x == point.x and second_point.y == point.y:
                    same += 1
                elif second_point.x == point.x:
                    vertical += 1
                else:
                    a,b = (second_point.y - point.y, second_point.x - point.x)
                    sign = 1 if a/b > 0 else -1
                    a,b = abs(a), abs(b)
                    g = gcd(a,b)
                    a,b = (a/g, b/g)
                    a = sign*a
                    cur[(a,b)] += 1
            curmax = same + max(max(cur.values()), vertical)
            ans = max(curmax, ans)
        return ans

inp = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
inp = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
inp = [[1,1],[1,1],[2,2],[2,2],[2,2]]
inp = [[1,1],[2,2],[3,3]]
inp = [[0,0],[0,1]]
inp = toPoint(inp)
print(Solution().maxPoints(inp))
