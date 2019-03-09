from collections import defaultdict
class Solution:
    def possibleBipartition(self, n: 'int', dislikes: 'List[List[int]]') -> 'bool':
        left, right = set(), set()
        for u,v in dislikes:
            if not left and not right:
                left .add(u)
                right.add(v)
            if (u in left and v in left) or (u in right and v in right):
                return False
            elif u in left:
                right.add(v)
            elif u in right:
                left.add(v)
            elif v in left:
                right.add(u)
            elif v in right:
                left.add(u)
        return True

n = 4
inp = [(1,2), (3,4), (1,3)]
print(Solution().possibleBipartition(n, inp))





        