class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def get_median(a, l, b):
            m = l>>1
            if l&1:
                return a[b+m]
            return (a[b+m-1]+a[b+m])/2

        def get_sorted_median(nums1, n1start, n1end, nums2, n2start, n2end):
            print(n1start, n1end, n2start, n2end)
            l1 = n1end - n1start + 1
            l2 = n2end - n2start + 1
            if l1>l2:
                nums1, nums2 = nums2, nums1
                n1start, n2start = n2start, n1start
                n1end, n2end = n2end, n1end
                l1, l2 = l2, l1

            if l1==1 and l2==1:
                return (nums1[n1start]+nums2[n2start])/2
            elif l1 == 1:
                l2_median = get_median(nums2, l2, n2start)
                if l2_median == nums1[0]:
                    return nums1[0]
                elif l2_median < nums1[0]:
                    return get_median(nums2, l2+1, n2start)
                else:
                    return get_median(nums2, l2-1, n2start)
            else:
                l1_mean = get_median(nums1, l1, n1start)
                l2_mean = get_median(nums2, l2, n2start)
                n1_mid = (n1end + n1start) >> 1
                n2_mid = (n2end + n2start) >> 1
                if l1_mean > l2_mean:
                    return get_sorted_median(nums1, n1start, n1_mid-(l1&1), nums2, n2_mid+1, n2end)
                else:
                    return get_sorted_median(nums1, n1_mid+1, n1end, nums2, n2start, n2_mid-(l2&1))
        return get_sorted_median(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1)


a1 = [1,2]
a2 = [5,6,7,8]
s = Solution()
print(s.findMedianSortedArrays(a1, a2))
