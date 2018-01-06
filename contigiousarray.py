class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        # (right, left) each entry
        for i in nums:
        	left = i-1
        	right = i+1
        	if i not in d:
        		d[i] = [None, None]
        	if left in d:
        		d[left][0] = i
        		d[i][1] = left

        	if right in d:
        		d[right][1] = i 
        		d[i][0] = right

        # print(d)

        max_count = 0
        visited = set()
        for k in d.keys():
        	if k not in visited:
	        	count = 1
	        	left = d[k][1]
	        	right = d[k][0]
	        	visited.add(k)
	        	while left is not None:
	        		visited.add(left)
	        		count += 1
	        		left = d[left][1]

	        	while right is not None:
	        		visited.add(right)
	        		right = d[right][0]
	        		count +=1 
	        	max_count = max(max_count, count)

        return max_count

a=[1,3,5]
s=Solution()
print(s.longestConsecutive(a))
