class StockSpanner(object):

    def __init__(self):
    	self.stk = []

        

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        c = 1
        while self.stk and  price > self.stk[-1][0]:
        	_, vc = self.stk.pop()
        	c+=vc
        self.stk.append((price, c))
        return c

        


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
print(obj.next(100))
print(obj.next(110))
print(obj.next(120))
print(obj.next(130))