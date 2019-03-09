from collections import defaultdict
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = defaultdict(list)
        

    def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
        self.map[key].append((timestamp, value))


    def get(self, key: 'str', timestamp: 'int') -> 'str':
        def binsearch(a, t):
            if a[-1][0] < t:
                return a[-1]
            if a[0][0] > t:
                return "", ""
            l = len(a)
            i,j = 0, l-1
            while i<=j:
                m = (i+j) >> 1
                if a[m][0] == t:
                    return a[m]
                elif a[m][0] < t:
                    i = m+1
                else:
                    j = m-1
            return a[i-1]
        if key not in self.map:
            return ""
        _, val = binsearch(self.map[key], timestamp)
        return val

        


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set(1,1,10)
obj.set(1,2,20)
# obj.set(1,3,30)
# obj.set(1,4,40)
print(obj.get(1,20))

# obj.set("love","high",10)
# obj.set("love","low",20)
# print(obj.get("love",5))
# print(obj.get("love",10))
# print(obj.get("love",15))
# print(obj.get("love",20))
# print(obj.get("love",25))

