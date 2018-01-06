class Node:
    def __init__(self, s, e):
        self.s = s
        self.e = e
        self.left = None
        self.right = None

class MyCalendar:

    def __init__(self):
        self.root = None

    def __book(self, start, end, cur):
        if cur.e <= start:
            if cur.right is not None:
                return self.__book(start, end, cur.right)
            else:
                cur.right = Node(start, end)
                return True
        elif cur.s >= end: 
            if cur.left is not None:
                return self.__book(start, end, cur.left)
            else:
                cur.left = Node(start, end)
                return True
        else:
            return False


    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.__book(start, end, self.root)


s=MyCalendar()
# print(s.book(1,10))
print(s.book(0,1))
print(s.book(2,3))
print(s.book(1,3))