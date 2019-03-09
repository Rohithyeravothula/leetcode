class Solution(object):
    def checkPossibility(self, a):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not a:
        	return True
        l = len(a)
        count = 0
        prev = None
        for i in range(l-1):
        	if a[i] > a[i+1]:
        		prev = i
        		count += 1
        i = prev
        # print(i, a[i], count)
        if count > 1:
        	return False

        if count == 0:
        	return True

        if i > 0 and i<(l+1) and a[i-1] < a[i+1]:
        	return True

        if (i+2) < l and a[i] < a[i+2]:
        	return True

        if i==0 or i==l-2:
        	return True

        return False
s = Solution()
inp = [4,50,60,8,9]
inp = [4,1,2,3]
inp = [4,10,2,3]
inp = [4,2,3,6]
inp = []
inp = [1,2,3,4]
print(s.checkPossibility(inp))
         