class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def get_median(ary):
        	l = len(ary)
        	if l == 1:
        		return ary[0]
        	if l%2 == 0:
        		return (ary[int(l/2)] + ary[l-int(l/2)])/2
        	else:
        		return ary[int(l/2)]

        def find_median(a,b):
        	# print(a,b)
        	l_a = len(a)
        	l_b = len(b)
        	# print(l_a, l_b)
        	if l_a == 1 and l_b == 1:
        		return (a[0] + b[0]) / 2
        	elif l_a == 0:
        		return get_median(b)
        	elif l_b == 0:
        		return get_median(a)
        	m_a = get_median(a)
        	m_b = get_median(b)
        	if m_a == m_b:
        		return m_a
        	elif m_a<m_b:
        		i_a = int(l_a/2)
        		i_b = l_b-int(l_b/2)
        		# print(i_a, i_b, a[i_a:], b[:i_b], lb-int(l_b/2))
        		return find_median(a[i_a:], b[:i_b])
        	else:
        		i_a = l_a-int(l_a/2)
        		i_b = int(l_b/2)
        		return find_median(a[:i_a], b[i_b:])
        return find_median(nums1, nums2)

a=[100]
b=[4,5,6]
s=Solution()
print(s.findMedianSortedArrays(a,b))
