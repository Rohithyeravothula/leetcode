class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return "({}, {})".format(self.start, self.end)

    def __repr__(self):
        return str(self)

class Solution:
    def insert(self, intervals_format, newInterval_format):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals = []
        for i in intervals_format:
            intervals.append([i.start, i.end])
        intervals.append([newInterval_format.start, newInterval_format.end])

        if len(intervals) == 0 or len(intervals) == 1:
            return [newInterval_format]

        def compare_and_merge(left, right):
            if (left[1] <= right[1] and left[1] >= right[0]):
                return [(min(left[0], right[0]), max(left[1], right[1]))]
            if (left[0] <= right[1] and left[0] >= right[0]):
                return [(min(left[0], right[0]), max(left[1], right[1]))]
            if left[0] <= right[0] and left[1] >= right[1]:
                return [(min(left[0], right[0]), max(left[1], right[1]))]
            return [left, right]
        stk = []
        intervals.sort()
        for single_iter in intervals:
            if len(stk) == 0:
                stk.append(single_iter)
            else:
                top = stk.pop()
                stk.extend(compare_and_merge(top, single_iter))
        ans = []
        for e in stk:
            ans.append(Interval(e[0], e[1]))
        return ans

intervals=[Interval(1,3)]
new_inter = Interval(0,0)
s=Solution()
merged = s.insert(intervals, new_inter)
print(merged)