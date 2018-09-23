import math
class SegmentTree():
    def __init__(self, nums):
        self.nums = nums
        self.nums_length = len(nums)
        self.h = 1 + math.ceil(math.log(1+self.nums_length, 2))
        self.seg = [0]*(1 << self.h)
        self.seg_length = len(self.seg)
        self.build_seg_tree()

    def build_seg_tree(self):
        def build(a, i, l, r, nums):
            if l==r:
                a[i] = nums[l]
            elif l<r:
                m = (l+r) >> 1
                build(a, 2*i+1, l, m, nums)
                build(a, 2*i+2, m+1, r, nums)
                a[i] = a[2*i+1] + a[2*i+2]
        build(self.seg, 0, 0, self.nums_length-1, self.nums)

    def query_seg_tree(self, ql, qr):
        def query(a, i, l, r, ql, qr):
            if l>=ql and r<=qr:
                return a[i]
            elif l > qr or r < ql:
                return 0
            else:
                m = (l+r) >> 1
                return query(a, 2*i+1, l, m, ql, qr) + query(a, 2*i+2, m+1, r, ql, qr)
        return query(self.seg, 0, 0, self.nums_length-1, ql, qr)

    def update_seg_tree_with_diff(self, index, val):
        def update(a, i, l, r, index, diff):
            if index < l or index > r or i >= self.seg_length:
                return    
            elif l<=r:
                m = (l+r) >> 1
                a[i] += diff
                update(a, 2*i+1, l, m, index, diff)
                update(a, 2*i+2, m+1, r, index, diff)
            
        diff = val - self.nums[index]
        update(self.seg, 0, 0, self.nums_length-1,index, diff)
        self.nums[index] = val


    def update_seg_tree_with_val(self, index, val):
        def update(a, i, l, r, index, val):
            if index < l or index > r or i >= self.seg_length:
                return
            elif l<r:
                m = (l+r) >> 1
                build(a, 2*i+1, l, m, index, val)
                build(a, 2*i+2, m+1, r, index, val)
                a[i] = a[2*i+1] + a[2*i+2]



class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.seg = SegmentTree(nums)
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.seg.update_seg_tree_with_diff(i, val)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.seg.query_seg_tree(i, j)
        



# Your NumArray object will be instantiated and called as such:
# obj = NumArray([1,2,3,4,5])
# print(obj.sumRange(0, 3))
# obj.update(0, 4)
# print(obj.sumRange(0, 3))
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

obj = NumArray([-1])
print(obj.sumRange(0, 1))
obj.update(0, 0)
print(obj.sumRange(0, 1))
obj.update(0, -1)
print(obj.sumRange(0, 1))