class DoubleListNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        return "{} -> {}".format(self.key, self.val)

    def __repr__(self):
        return str(self)

class DoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, key, val):
        self.size += 1
        node = DoubleListNode(key, val)
        if self.head is None:
            self.tail = node
            self.head = node
        else:
            node.prev = self.head
            self.head.next = node
            self.head = node
        return node

    def delete(self, node):
        self.size -= 1
        left = node.prev
        right = node.next
        if left is not None and right is not None:
            left.next = right
            right.prev = left
        else:
            if left is None and right is None:
                self.head = None
                self.tail = None
            elif left is None:
                self.tail = node.next
                node.next = None
                self.tail.prev = None
            elif right is None:
                self.head = node.prev
                self.head.next = None
                node.prev = None
        node.next = None
        node.prev = None

    def __str__(self):
        if self is not None:
            return str("{} -> {}".format(self.key, self.val))
        return "None"

    def __repr__(self):
        return str(self)

    def pprint(self):
        cur = self.tail
        s=""
        while cur is not None:
            s = s+str(cur.val)+" "
            cur = cur.next
        print(s[:-1])



# test = DoubleLinkedList()
# for i in range(0, 10):
#   test.insert(i)
# test.pprint()
# test.delete(test.tail.next)
# test.pprint()

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.table = {}
        self.dll = DoubleLinkedList()
        self.capacity = capacity
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.table:
            value, node = self.table[key]
            self.dll.delete(node)
            node = self.dll.insert(key, value)
            self.table[key][1] = node
            return self.table[key][0]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.table:
            self.table[key][0] = value
            self.dll.delete(self.table[key][1])
            node = self.dll.insert(key, value)
            self.table[key] = [value, node]
            # accessed to make this most recently accessed one
        else:
            if self.capacity > self.dll.size:
                #insert into dll and table
                node = self.dll.insert(key, value)
                self.table[key] = [value, node]
            else:
                del self.table[self.dll.tail.key]
                self.dll.delete(self.dll.tail)
                # delete this entry from table
                node = self.dll.insert(key, value)
                self.table[key] = [value, node]
                #del tail from dll and insert 
        # print(self.table[key][1].val, self.table[key][1].next, self.table[key][1].prev)
    def pprint(self):
        self.dll.pprint()



lru = LRUCache(1)
lru.put(2,1)
print(lru.get(2))
# for i in range(0, 7):
#     lru.put(i, i)

# lru.pprint()
# for i in range(2, 5):
#     lru.get(i)

# lru.pprint()
# for j in range(0, 7):
#     lru.put(j, j)

# lru.pprint()
