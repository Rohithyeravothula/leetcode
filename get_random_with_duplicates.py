from random import randint
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.seen = {}
        self.values = []
        self.length = -1

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.length+=1
        self.values.append(val)
        if val in self.seen:
            self.seen[val].add(self.length)
            return False
        else:
            self.seen[val] = {self.length}
            return True

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.seen:
            index = self.seen[val].pop()
            self.seen[self.values[self.length]].add(index)
            self.seen[self.values[self.length]].remove(self.length)
            self.values[self.length], self.values[index] = self.values[index], self.values[self.length]
            self.length -= 1
            self.values.pop()
            if not self.seen[val]:
                del self.seen[val]
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.values[randint(0, self.length)]
        


# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
obj.insert(9)
obj.insert(9)
obj.insert(1)
obj.insert(1)
obj.insert(2)
obj.insert(1)
obj.remove(1)
print(obj.seen, obj.values)
obj.remove(2)
obj.insert(9)
obj.remove(1)
obj.getRandom()
print(obj.seen, obj.values)