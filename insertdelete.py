import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pos={}
        self.data = []
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            self.data.append(val)
            self.pos[val] = len(self.data)-1
            return True
        else:
            return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if len(self.data) == 1 and self.data[0] == val:
            self.data = []
            self.pos = {}
            return True
        elif val in self.pos:
            p = self.pos[val]
            le = self.data[-1]
            self.data[p] = le
            self.pos[le] = p
            del self.data[-1]
            return True
        else:
            return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.data[random.randint(0, len(self.data)-1)]


s=RandomizedSet()
print(s.remove(0))
print(s.remove(0))
print(s.insert(0))
print(s.getRandom())
print(s.remove(0))
print(s.insert(0))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()