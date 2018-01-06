class MyCalendar:

    def __init__(self):
        self.timings = {}

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if start in self.timings:
        	return False
        else:
        	for s,e in self.timings.items():
        		if start < e and end > s:
        			return False
        	self.timings[start] = end
        	return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
s=MyCalendar()
# print(s.book(1,10))
print(s.book(0,1))
print(s.book(2,3))
print(s.book(1,3))