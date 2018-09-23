class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if not tree:
        	return 0
        l = len(tree)
        i = 0
        max_count = 1
        j=0
        while i<l and j<l:
        	b1 = tree[i]
        	b2 = -1
        	count = 1
        	j = i+1
        	candidate = j
        	while j<l:
        		if tree[j] != b1 and b2 == -1:
        			b2 = tree[j]
        		if tree[j] not in {b1, b2}:
        			break
        		if tree[j] != tree[j-1]:
        			candidate = j
        		j+=1
        		count+=1
        	max_count = max(max_count, count)
        	i = candidate
        return max_count

# inp = [1,0,1,4,1,4,1,2,3]
# inp = [1,2,1,4,4]
inp = [1,2,1]
inp = [0,2,3,2,2]
inp = [1,2,3,2,2]
inp = [3,3,3,1,2,1,1,2,3,3,4]
inp = [1,2,1,2,1,2]
inp = []
print(Solution().totalFruit(inp))

