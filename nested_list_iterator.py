class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.data = self.flatten(nestedList)
        l = len(nestedList)
        for i in range(0, l):
            nestedList[i] = self.data[i]

        nestedList.extend(self.data[i-1:])
        self.nestedList = nestedList

        # print(self.data)

    def flatten(self, a):
        ans = []
        for i in a:
            if isinstance(i, list):
                ans.extend(self.flatten(i))
            else:
                ans.append(i)
        return ans

    def next(self):
        """
        :rtype: int
        """
        return self.nestedList.pop()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return not self.nestedList == []

s=NestedIterator([1,2,[3,4], [[5]]])
print(s.next())
print(s.hasNext())
# print(flatten())
