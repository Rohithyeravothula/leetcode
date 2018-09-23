# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "({}, {})".format(self.start, self.end)

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        l,i = len(intervals),0
        merged = []
        if newInterval.end < intervals[i].start or newInterval.start < intervals[i].start:
            merged.append(newInterval)
        if not merged:
            while i<l and intervals[i].end < newInterval.start:
                merged.append(intervals[i])
                i+=1
            if i<l:
                top = intervals[i]
                if newInterval.end >= top.start:
                    merged.append(Interval(min(top.start, newInterval.start), max(top.end, newInterval.end)))
                else:
                    merged.append(newInterval)
                    merged.append(top)
                    i+=1
        while i<l:
            top = merged[-1]
            cur = intervals[i]
            if top.end >= cur.start:
                merged.pop()
                merged.append(Interval(top.start, max(top.end, cur.end)))
            else:
                merged.append(cur)
            i+=1
        if merged[-1].end < newInterval.start:
            merged.append(newInterval)
        return merged
            

inp = [Interval(2, 3), Interval(12, 15)]
insp = Interval(16, 115)
print(Solution().insert(inp, insp))