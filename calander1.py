class MyCalendar:

    def __init__(self):
        self.intervals = []

    def check(self, start, end):
        l = len(self.intervals)
        for i in range(0, l):
            cur_start = self.intervals[i][0]
            cur_end = self.intervals[i][1]
            if cur_start <= start and cur_start > end:
                return False
            elif cur_end > start and cur_end < end:
                return False
            elif cur_start <= start and cur_end > end:
                return False
            elif start < cur_end and start > cur_start:
                return False
            elif end > cur_start and end < cur_end:
                return False
            elif start > cur_start and end < cur_end:
                return False
            elif start < cur_start and end > cur_start:
                return False
            elif end < cur_end and end > cur_start:
                return False
        return True

       
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bools
        """
        if self.check(start, end):
            self.intervals.append([start, end])
            return True
        return False

# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
obj.book(5, 21)
obj.book(3,21)
print(obj.intervals)