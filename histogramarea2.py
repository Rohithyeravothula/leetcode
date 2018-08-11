import math
class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        def construct(tree, index, left, right):
        	# print(index, left, right)
        	if left == right:
        		tree[index] = heights[left]
        	else:
        		mid = (left+right)//2
        		construct(tree, 2*index+1, left, mid)
        		construct(tree, 2*index+2, mid+1, right)
        		tree[index] = min(tree[2*index+1], tree[2*index+2])

        def get_min(seg_tree, sl, sr):
        	def __min(seg_tree, index, left, right, search_left, search_right):
        		if search_left <= left and search_right >= right:
        			return seg_tree[index]
        		elif search_left > right or search_right < left:
        			return float("inf")
        		else:
        			mid = (left+right)//2
        			left = __min(seg_tree, 2*index+1, left, mid, search_left, search_right)
        			right = __min(seg_tree, 2*index+2, mid+1, right, search_left, search_right)
        			return min(left, right)
        	return __min(seg_tree, 0, 0, len(heights)-1, sl, sr)

        def get_seg_tree(inp):
        	seg_l = 2*int(math.pow(2, 1+int(math.log2(len(inp)))))
        	seg_tree = [float("inf")]*seg_l
        	construct(seg_tree, 0, 0, len(inp)-1)
        	return seg_tree

        def max_area(inp):
        	def __max(inp, left, right):
        		if left == right:
        			return inp[left]
        		else:
        			mid = (left+right)//2

        	inp_seg = get_seg_tree(inp)




inpheights = [1,4,2,3,5]
s=Solution()
print(s.largestRectangleArea(inpheights))
