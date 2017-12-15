import math
class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.numbers = nums
        self.length = len(self.numbers)
        if self.length > 0:
            self.seglength = 2**(int(math.log(self.length<<1, 2))+1)-1
            print(self.seglength)
        else:
            self.seglength = 0
        self.segtree = [0]*self.seglength
        # print(self.seglength, int(math.log(self.length<<1, 2)))

        def seg_tree():
            def __seg_tree(seg, i, s, e, a, n):
                # print(n, i, s, e, seg)
                if s == e:
                    seg[i] = a[s]
                elif s<e:
                    __seg_tree(seg, 2*i+1, s, int((s+e)/2), a, n)
                    __seg_tree(seg, 2*i+2, 1+int((s+e)/2), e, a, n)
                    seg[i] = seg[2*i+1] + seg[2*i+2]

            __seg_tree(self.segtree, 0, 0, self.length-1, self.numbers, self.seglength)
        seg_tree()



# 
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        def __update(seg, i, s, e, j, diff, n): 
            # print(i, s, e, j, diff) 
            if s<=j and e>=j:
                seg[i] = seg[i] + diff
                if s!=e:
                    __update(seg, 2*i+1, s, int((s+e)/2), j, diff, n)
                    __update(seg, 2*i+2, 1+int((s+e)/2), e, j, diff, n)
        diff = val - self.numbers[i]
        __update(self.segtree, 0, 0, self.length-1, i, diff, self.seglength)
        self.numbers[i] = val
        # print(self.segtree)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        def __get_sum_recr(seg, i, rs, re, s, e, n):
            # no overlap
            if re < s or e < rs:
                return 0
            # total overlap
            elif s<=rs and e>=re:
                return seg[i]
            # partial overlap
            else:
                return __get_sum_recr(seg, 2*i+1, rs, int((rs+re)/2), s, e, n) + __get_sum_recr(seg, 2*i+2, 1+int((rs+re)/2), re, s ,e, n)

        return __get_sum_recr(self.segtree, 0, 0, self.length-1, i, j, self.seglength)


# Your NumArray object will be instantiated and called as such:
# ["NumArray","sumRange","update","sumRange","sumRange","update","update","sumRange","sumRange","update","update"]
# [[5,6],[9,27],[2,3],[6,7],[1,-82],[3,-72],[3,7],[1,8],[5,13],[4,-67]]
nums = [1,2,3,4]
# nums = [i for i in range(1, 9)]
# print(sum(nums[5:7]))
obj = NumArray(nums)
print(obj.segtree)
# obj.update(9,27)
# obj.update(1,-82)
# obj.update(3,-72)
# print(obj.sumRange(1, 8))
# print(sum(nums[1:9]))
# print(obj.segtree)
# print(obj.sumRange(5, 9))

# print(obj.sumRange(2,3))
# obj.update(1,-4)
# print(obj.sumRange(0, 1))

