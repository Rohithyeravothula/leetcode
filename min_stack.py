class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = None
        self.values = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.min is None:
            self.min = x 
            self.values.append(0)
        else:
            self.values.append(x - self.min)
            if self.min > x:
                self.min = x

    def pop(self):
        """
        :rtype: void
        """
        if self.values[-1] < 0:
            self.min = self.min - self.values[-1]
        self.values.pop()
        if not self.values:
            self.min = None
        

    def top(self):
        """
        :rtype: int
        """
        if self.values[-1] < 0:
            return self.min
        return self.values[-1] + self.min
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
# obj.push(6)
# obj.push(8)
# obj.push(4)
# obj.push(1)
# obj.push(3)
# obj.pop()
# obj.pop()
# obj.pop()
# obj.pop()
# obj.pop()
# print(obj.top())
obj.push(0)
obj.push(1)
obj.push(0)
print(obj.values, obj.min)
print(obj.getMin())
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()