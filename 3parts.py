class Solution:
    def threeEqualParts(self, a):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        l = len(a)
        if not a or l<3:
        	return [-1,-1]


        a="".join(map(str,a))
        left = [0]
        for i in range(l):
        	left.append((left[-1]<<1)+(int(a[i])))

        right = [0]*l
        right[l-1] = int(a[l-1])
        b=0
        for i in range(l-2, -1, -1):
        	right[i] = (2<<b)*int(a[i]) + right[i+1]
        	b+=1
        print(right)


        for i in range(0, l):
        	cur_val = left[i+1]
        	j = i+2
        	while j<l:
        		print(i, j, left[i+1], right[j])
        		mid_val = int(a[i+1:j],2)
        		if mid_val > cur_val or right[j] < cur_val or right[j] < mid_val:
        			break
        		elif mid_val == cur_val and right[j] == mid_val:
        			return [i,j]
        		j+=1
        return [-1,-1]

inp =[1,1,1]
inp = [1,1,0,1,1]
inp = [1,1,1,1,1,1,0,1,1,1]
inp = [1,0,1,0,1]
print(Solution().threeEqualParts(inp))



