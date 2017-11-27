class MyCalendar:

    def __init__(self):
        self.intervals = []

    def check(self, start, end):
        l = len(self.intervals)
        for i in range(0, l):
            # print(cur_start, cur_end, start, end)
            cur_start = self.intervals[i][0]
            cur_end = self.intervals[i][1]
            if start <= cur_start:
                if end > cur_start:
                    return False
            elif start > cur_start and start < cur_end:
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
obj.book(10, 20)
obj.book(20, 34)
# obj.book(3,4)
obj.book(3,11)
obj.book(3,22)
obj.book(10, 20)
obj.book(10, 14)
obj.book(10, 25)
obj.book(12, 18)
obj.book(12, 22)
obj.book(20, 21)
obj.book(10, 40)
print(obj.intervals)


