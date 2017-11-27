# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return "({}, {})".format(self.start, self.end)

    def __repr__(self):
        return str(self)

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        l=len(intervals)
        if l < 2:
            return intervals
        intervals = sorted(intervals, key=lambda x:x.start)
        stack = [intervals[0]]
        print(intervals)
        for i in range(1, l):
            if stack[-1].start == intervals[i].start:
                if stack[-1].end < intervals[i].end:
                    stack[-1].end = intervals[i].end
            elif stack[-1].end >= intervals[i].start:
                if stack[-1].end < intervals[i].end:
                    stack[-1].end = intervals[i].end
            else:
                stack.append(intervals[i])

        print(stack)
        return stack

a=[[1,4], [2,3]]

for i in range(0, len(a)):
    a[i] = Interval(a[i][0], a[i][1])
# a=sorted(a, key=lambda x:x.start)
# print(a)
s=Solution()
s.merge(a)
