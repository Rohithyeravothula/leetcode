# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
    	return "({}, {})".format(self.start, self.end)

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        l = len(intervals)
        if l < 1:
        	return intervals
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        stk = [sorted_intervals[0]]
        i = 1
        while i<l:
        	cur = sorted_intervals[i]
        	top = stk[-1]
        	if top.end < cur.start:
        		stk.append(cur)
        	else:
        		top = stk.pop()
        		stk.append(Interval(top.start, max(top.end, cur.end)))
        	i+=1
        return stk


inter = [[1,2]]
ii = list(map(lambda x: Interval(x[0], x[1]), inter))
s=Solution()
print(s.merge(ii))