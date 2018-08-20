class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ele_stack = []
        self.min_stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.ele_stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        else:
            self.min_stack.append(min(x, self.min_stack[-1]))


    def pop(self):
        """
        :rtype: void
        """
        self.ele_stack.pop()
        self.min_stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.ele_stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-1)
print(obj.getMin())
obj.pop()
print(obj.min_stack, obj.ele_stack)
print(obj.getMin())
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()