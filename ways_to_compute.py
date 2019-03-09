from operator import add, sub, mul, floordiv
from collections import defaultdict
class Solution(object):
    def diffWaysToCompute(self, cur):
        """
        :type input: str
        :rtype: List[int]
        """
        operators = {'+', '-', '*', '/'}
        opm = {'+':add, '-':sub, '*':mul, '/':floordiv}
        def evaluate(cur, prev):
            if cur in prev:
                return prev[cur]

            op_found = False
            for i, val in enumerate(list(cur)):
                if val in operators:
                    op_found = True
                    evaluate(cur[:i], prev)
                    evaluate(cur[i+1:], prev)
                    for c1 in prev[cur[:i]]:
                        for c2 in prev[cur[i+1:]]:
                            prev[cur].append(opm[cur[i]](c1, c2))
            if not op_found:
                prev[cur] = [int(cur)] if cur else []

        seen = []
        self.memo = defaultdict(list)
        op_found = False
        for i, val in enumerate(list(cur)):
            if val in operators:
                op_found = True
                evaluate(cur[:i], self.memo)
                evaluate(cur[i+1:], self.memo)
                for c1 in self.memo[cur[:i]]:
                    for c2 in self.memo[cur[i+1:]]:
                        seen.append(opm[cur[i]](c1, c2))
        if not op_found:
            seen.append(int(cur))
        seen.sort()
        return seen

inp = "2*3+4-7"
inp = "2-1-1"
inp = "2*3-4*5"
inp = "3"
inp = "15+7-6*24"
inp = "2+3"
print(Solution().diffWaysToCompute(inp))


