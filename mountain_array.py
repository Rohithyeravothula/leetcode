class Solution:
    def validMountainArray(self, a):
        """
        :type A: List[int]
        :rtype: bool
        """
        l = len(a)
        if l<3:
        	return False
        i=1
        while i<l:
        	if a[i] <= a[i-1]:
        		break
        	i+=1

        if i==1 or i==l:
        	return False

        while i<l:
        	if a[i] >= a[i-1]:
        		break
        	i+=1

        # print(i)

        if i==l:
        	return True
        return False

inp = [1,2,3,4,5,3,2]
inp = [0,3,2,1]
inp = [4,5,4,3]
print(Solution().validMountainArray(inp))
