from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []
        self.right = []
        self.lc, self.rc = 0,0

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if self.lc == 0:
            heappush(self.left, -num)
            self.lc += 1
        elif num <= -self.left[0] and self.lc == self.rc:
            heappush(self.left, -num)
            self.lc += 1
        elif num <= -self.left[0] and self.lc == self.rc+1:
            heappush(self.left, -num)
            heappush(self.right, -heappop(self.left))
            self.rc += 1
        elif num > -self.left[0] and self.lc == self.rc:
            heappush(self.right, num)
            heappush(self.left, -heappop(self.right))
            self.lc += 1
        else:
            heappush(self.right, num)
            self.rc += 1
        
    def findMedian(self):
        """
        :rtype: float
        """
        print(self.left, self.right)
        if self.lc == self.rc:
            return (-self.left[0] + self.right[0])/2
        else:
            return -self.left[0]/1



        


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
for i in range(1, 8):
    obj.addNum(3)
print(obj.findMedian())