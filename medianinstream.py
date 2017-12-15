import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """ 
        self.left = [] # max heap
        self.right = [] # min heap
        
    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.right) == 0:
            heapq.heappush(self.right, num)
        elif len(self.left) == 0:
            if num <= self.right[0] == 0:
                heapq.heappush(self.left, -1*num)
            else:
                heapq.heappush(self.left, -1*heapq.heappushpop(self.right, num))
        elif len(self.left) == len(self.right):
            if num >= self.right[0]:
                heapq.heappush(self.right, num)
            else:
                heapq.heappush(self.right, -1*heapq.heappushpop(self.left, -1*num))
        elif len(self.left)+1 == len(self.right):
            if num >= self.right[0]:
                heapq.heappush(self.left, -1*heapq.heappushpop(self.right, num))
            else:
                heapq.heappush(self.left, -1*num)
        print(self.left, self.right)


    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.left) == 0 and len(self.right) == 0:
            return None
        elif len(self.left) == 1 and len(self.right) == 0:
            # print(self.left)
            return -1*self.left[0]
        elif len(self.left) == 0 and len(self.right) == 1:
            return float(self.right[0])
        else:
            if len(self.left) == len(self.right):
                # print(len(self.left), len(self.right))
                return (-1*self.left[0] + self.right[0])/2
            return float(self.right[0])
        
# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
# obj.addNum(3)
# obj.addNum(4)
# obj.addNum(5)
# obj.addNum(1)
# obj.addNum(1)
# obj.addNum(1)
print(obj.findMedian())