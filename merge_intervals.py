class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = [intervals[0]]
        l = len(intervals)
        i = 1
        while i<l:
        	prev = result[-1]
        	cur = intervals[i]
        	if prev.end < cur.start:
        		result.append(cur)
        	else:
        		result.pop()
        		result.append(Interval(prev.start, max(prev.end, cur.end)))
        	i+=1
        return result
