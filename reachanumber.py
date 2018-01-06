class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target == 0:
        	return 0
        if abs(target) == 1:
        	return 1
        if abs(target) == 2:
        	return 3
        if abs(target) == 3:
        	return 2

        i = 3
        target = abs(target)
        while True:
        	num = (i*(i+1))//2
        	if num%2 == target%2 and num >= target:
        		return i
        	i+=1


s=Solution()
i=8
print(i, s.reachNumber(i))

# for i in range(0,10):
# 	print(i, s.reachNumber(i))

