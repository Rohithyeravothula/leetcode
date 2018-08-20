class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def get_sol(a, start, end, n):
        	if n == 0:
        		return [[]]
        	elif n < 0:
        		return None
        	result = []
        	for i in range(start, end):
        		cur_sol = get_sol(a, i, end, n-a[i])
        		if cur_sol:
	        		for sol in cur_sol:
	        			result.append([a[i]] + sol)
        	if not result:
        		return None
        	return result

        result = get_sol(candidates, 0, len(candidates), target)
        if result is None:
        	return []
        return result

s = Solution()
print(s.combinationSum([], 8))