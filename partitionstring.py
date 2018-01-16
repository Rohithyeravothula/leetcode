class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        d={}
        for i in S:
        	if i in d:
        		d[i]+=1
        	else:
        		d[i] = 1
        ans = []
        while True:
        	l = len(d)
        	curmin_key = min(d)
        	curmin_val = d[curmin_key]
        	ans.extend([l]*curmin_val)
        	for k in d:
        		if d[k] == curmin_val:
        			del d[k]
        		else:
        			d[k] -= curmin_val
        	if len(d)==0:
        		break
        return ans

input_string="a"
s=Solution()
print(s.partitionLabels(input_string))
