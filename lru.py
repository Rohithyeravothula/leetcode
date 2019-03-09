class DLLNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DLL(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, node):
        if not self.head:
            self.head = node
            self.tail = node 
        else:
            self.head.next = node
            node.prev = self.head
            self.head = node

    def add(self, val):
        node = DLLNode(val)
        self.addNode(node)
        return node

    def deleteNode(self, node):
        if node == self.tail:
            if self.head == node:
                self.tail, self.head = None, None
            else:
                self.tail = self.tail.next
        elif node == self.head:
            self.head = self.head.prev
        else:
            prev = node.prev
            prev.next = node.next
            node.next.prev = prev

    def trimTail(self):
        node = self.tail
        self.tail = self.tail.next
        return node

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dll = DLL()
        self.mapper = {}
        self.capacity = capacity
        self.count = 0
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.mapper:
            node = self.mapper[key]
            self.dll.deleteNode(node)
            self.dll.addNode(node)
            return self.mapper[key].val[1]
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.mapper:
            node = self.mapper[key]
            self.dll.deleteNode(node)
            node.val = (key, value)
            self.dll.addNode(node)
        else:
            if self.count == self.capacity:
                node = self.dll.trimTail()
                del self.mapper[node.val[0]]
                self.count -= 1
            node = self.dll.add((key, value))
            self.mapper[key] = node
            self.count += 1




# d = DLL()
# n1=d.add(1)
# n2=d.add(2)
# print(d.tail.val, d.tail.next.val, d.head.val, d.head.prev.val)
# d.deleteNode(n2)
# print(d.tail.val, d.head.val)