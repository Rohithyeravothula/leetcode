class Solution(object):
    def numSubarraysWithSum(self, a, s):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        if not a or sum(a) < s:
        	return 0

        

        i,j=0,0
        l = len(a)
        
        if s==0:
        	i=0
        	count = 0
        	while i<l:
        		p0=0
        		while i<l and a[i] == 0:
        			i+=1
        			p0+=1
        		count += (p0*(p0+1))//2
        		i+=1
        	return count

        c=0
        while j<l and c!=s:
        	c+=a[j]
        	j+=1

        count = 0
        while i<l and j<l:
        	p0 = 0
        	while i<l and a[i]!=1:
        		p0+=1
        		i+=1

        	p1 = 0
        	while j<l and a[j]!=1:
        		j+=1
        		p1 +=1

        	# print(i,j,p0,p1)
        	count += (p1+1)*(p0+1)
        	i+=1
        	j+=1

        # print(count)
        if a[-1] == 1:
	        p0 = 0
	        while i<l and a[i]!=1:
	        	p0+=1
	        	i+=1
	        count += (p0+1)
        return count

a,s = [1,0,0,0,0,1], 2 
print(Solution().numSubarraysWithSum(a, s))