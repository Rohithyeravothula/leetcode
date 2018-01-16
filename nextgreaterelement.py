class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stk = []
        l = len(nums2)
        ans = [-1]*l
        i = 0
        while i<l:
        	if len(stk) == 0:
        		stk.append(i)
        	else:
        		top = stk[-1]
        		if nums2[top] < nums2[i]:
        			ans[top] = nums2[i]
        			stk.pop()
        		else:
        			stk.append(i)
        			i+=1
        d={}
        for i in range(0, l):
        	d[nums2[i]] = ans[i]

        result = []
        for i in nums1:
        	result.append(d[i])
        return result


nm1 = [1,2,3]
nm2 = [1,2,3]
s=Solution()
print(s.nextGreaterElement(nm1, nm2))

