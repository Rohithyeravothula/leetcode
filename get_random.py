from random import randint
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.seen = {}
        self.values = []
        self.length = 0
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        print(self.seen)
        if val not in self.seen:
            self.seen[val] = self.length
            self.values.append(val)
            self.length += 1
            return True
        return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.seen:
            self.seen[self.values[self.length-1]] = self.seen[val]
            self.values[self.length-1], self.values[self.seen[val]] = self.values[self.seen[val]], self.values[self.length-1]
            self.values.pop()
            del self.seen[val]
            self.length -= 1
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.values[randint(0, self.length-1)]
        
        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_1 = obj.insert(2)
param_2 = obj.remove(1)
# print(obj.seen, obj.values, obj.length)
param_1 = obj.insert(2)
print(param_1)
# param_2 = obj.remove(2)
# param_3 = obj.getRandom()