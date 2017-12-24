class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append([x, min(self.min, x)])
        self.min = min(x, self.min)
        

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop[0]
        if len(self.stack) != 0:
            self.min = self.stack[-1][1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()