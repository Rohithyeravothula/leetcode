class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        l = len(pushed)
        cur = []
        i,j=0,0
        while i<=l and j<l:
        	if cur and cur[-1] == popped[j]:
        		cur.pop()
        		j+=1
        	elif i<l:
        		cur.append(pushed[i])
        		i+=1
        	else:
        		return False
        	# print(cur)
        if not cur:
        	return True
        return False

pu,po = [1,2,3], [2,1,3]
pu, po = [1,2,3,4,5],[4,3,5,1,2]
pu,po = [1],[2]
print(Solution().validateStackSequences(pu, po))