import math
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.seg, self.sl = self.build_segment_tree(nums)
        self.nums = nums

    def build_segment_tree(self, a):
        if not a:
            return [],0
        l = len(a)
        sl = 2**int(math.log((l<<2), 2))
        seg = [0]*(sl-1)
        def build(s, sl, a, al, l, r, i):
            if l >= al or i >= sl:
                return
            elif l==r:
                s[i] = a[l]
            else:
                m = (l+r)>>1
                build(s,sl, a, al, l, m, 2*i+1)
                build(s,sl, a, al, m+1, r, 2*i+2)
                s[i] = s[2*i+1] + s[2*i+2]
        build(seg,sl, a, l, 0, (sl>>1)-1, 0)
        return seg, sl-1
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        def update_seg(cl, cr, i, ui, val):
            if cl==cr and cl==ui:
                self.seg[i] += val
            elif cl <= ui and ui <= cr:
                self.seg[i] += val
                m=(cl+cr)>>1
                update_seg(cl, m, 2*i+1, ui, val)
                update_seg(m+1, cr, 2*i+2, ui, val)
            return 
        update_seg(0, self.sl>>1, 0, i, val-self.nums[i])
        self.nums[i] = val

        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        def get_sum(cl, cr, l, r, i):
            # print(cl, cr, l, r, i)
            if l<=cl and cr<=r:
                return self.seg[i]
            elif cr<l or r<cl:
                return 0
            else:
                m = (cl+cr)>>1
                return get_sum(cl, m, l, r, 2*i+1) + get_sum(m+1, cr, l, r, 2*i+2)
        return get_sum(0, self.sl>>1, i, j, 0)


        


# Your NumArray object will be instantiated and called as such:
# nums = [3,4,6,5,2]
nums=[]
nums = []
obj = NumArray(nums)
# print(obj.sumRange(0,2))
# obj.update(1,2)
# print(obj.sumRange(0,2))
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)