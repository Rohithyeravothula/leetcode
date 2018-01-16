class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def subsets(a):
        	if len(a) == 0:
        		return [[]]
        	if len(a) == 1:
        		return [[], a]
        	else:
        		cur = a[0]
        		i = 1
        		l = len(a)
        		while i<l and a[i] == cur:
        			i+=1
        		tmp = [a[0]]
        		cursubsets = [tmp]
        		for j in range(1, i):
        			tmp = tmp + [a[0]]
        			cursubsets.append(tmp)
        		# print(cursubsets)
        		rest = subsets(a[i:])
        		new = rest[:]
        		for ss in rest:
        			for pp in cursubsets:
	        			new.append(pp + ss)
        		return new

        if len(nums) == 0:
        	return [[]]
        elif len(nums) == 1:
        	return [[], nums]
        nums.sort()
        return subsets(nums)
s=Solution()
print(s.subsetsWithDup([1,1,1,1]))