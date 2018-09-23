import math
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left, self.right = None,None

class SegmentTree():
    def __init__(self, nums):
        self.nums_l = len(nums)
        self.nums = nums
        h = 1 + math.ceil(math.log(self.nums_l, 2))
        self.t = [0]*(1 << h)

    def build_seg_tree(self):
        def build(a, i, l, r, nums):
            # print(a, i, l, r)
            if l==r:
                a[i] = nums[l]
            elif l<r:
                m = (l+r) >> 1
                build(a, 2*i+1, l, m, nums)
                build(a, 2*i+2, m+1,r, nums)
                a[i] = max(a[2*i+1], a[2*i+2])
        build(self.t,0, 0, self.nums_l-1, self.nums)

    def query_seg_tree(self, ql, qr):
        def query(a, i, l, r, ql, qr):
            if l >= ql and r <= qr:
                return a[i]
            elif l > qr or r < ql:
                return -1*float("inf")
            else:
                m = (l+r) >> 1
                return max(query(a, 2*i+1, l, m, ql, qr), query(a, 2*i+2, m+1, r, ql, qr))
        return query(self.t, 0, 0, self.nums_l-1, ql, qr)


class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        l = len(nums)
        st = SegmentTree(nums)
        st.build_seg_tree()
        inv_nums = {}
        for i, v in enumerate(nums):
            inv_nums[v] = i
        def build(a, l, r, inva, segtree):
            if l == r:
                return TreeNode(nums[l])
            elif l>r:
                return None
            else:
                m = segtree.query_seg_tree(l, r)
                mi = inva[m]
                cur = TreeNode(m)
                cur.left = build(a, l, mi-1, inva, segtree)
                cur.right = build(a, mi+1, r, inva, segtree)
                return cur
        return build(nums, 0, l-1, inv_nums, st)

        

# s = Solution()
# s.constructMaximumBinaryTree([1])

s = SegmentTree([1,2,3,4,4])
s.build_seg_tree()
print(s.t)
# print(s.query_seg_tree(0, 900))
