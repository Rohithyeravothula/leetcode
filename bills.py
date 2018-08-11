class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        c5, c10 = 0, 0
        for b in bills:
        	if b == 5:
        		c5+=1
        	elif b == 10:
        		c10+=1
        		if c5>0:
	        		c5-=1
	        	else:
	        		return False
        	elif b==20:
        		if c10>0 and c5>0:
        			c10-=1
        			c5-=1
        		elif c5>2:
        			c5-=3
        		else:
        			return False
        return True
bs = [5, 5, 5 ,10, 20]
s = Solution()
print(s.lemonadeChange(bs))