from collections import defaultdict
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for h,k in people:
        	res.insert(k, (h,k))
        return res

inp = [[1,1]]
inp = [[6,0], [7,0], [4,1]]
inp = []
inp = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(Solution().reconstructQueue(inp))