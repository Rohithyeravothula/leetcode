class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.length = len(nums)
        self.sums = [0]*(self.length)
        if self.length != 0:
            self.sums[0] = nums[0]
            for i in range(1, self.length):
                self.sums[i] = self.sums[i-1] + self.nums[i]
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if self.length != 0:
            if i == 0:
                return self.sums[j]
            return self.sums[j] - self.sums[i-1]
        else:
            return 0

        


# Your NumArray object will be instantiated and called as such:
a=[-2,0,3,-5,2,-1]
obj = NumArray(a)
print(obj.sums)
