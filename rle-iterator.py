class RLEIterator(object):

    def __init__(self, a):
        """
        :type A: List[int]
        """
        self.a = a
        self.index = 0
        self.length = len(self.a)
        

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.index >= self.length:
        	return -1
        elif self.a[self.index] == 0:
        	self.index += 2
        	return self.next(n)
        elif self.a[self.index] == n:
        	self.a[self.index] = 0
        	self.index += 2
        	return self.a[self.index-1]
        elif self.a[self.index] < n:
        	n -= self.a[self.index]
        	self.a[self.index] = 0
        	self.index += 2
        	return self.next(n)
        else:
        	self.a[self.index] -= n
        	return self.a[self.index+1]

        


# Your RLEIterator object will be instantiated and called as such:
obj = RLEIterator([0,1,0,4])
print(obj.next(2))
# print(obj.a)
print(obj.next(1))
print(obj.next(1))
print(obj.next(1))
print(obj.next(1))
print(obj.next(1))