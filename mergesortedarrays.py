class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        nums2 = nums2[::-1]
        j = 0
        # end_start = m 
        end_end = len(nums1)-1
        while i>=0 and j<n:
        	if nums1[i] > nums2[j]:
        		nums1[end_end] =nums1[i]
        		end_end-=1
        		#end_start-=1
        		i-=1
        	else:
        		nums1[end_end] = nums2[j]
        		j+=1
        		end_end-=1
        while j<n:
        	nums1[end_end] = nums2[j]
        	j+=1
        	end_end-=1


s=Solution()
left = [4,8,10,12,0,0,0,0,0]
right = [1,2,6,9,15]
s.merge(left, 4, right, 5)
print(left)
