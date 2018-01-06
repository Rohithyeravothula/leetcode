import math
class Solution(object):
    def ipToCIDR(self, ipstr, range):
        """
        :type ip: str
        :type range: int
        :rtype: List[str]
        """
        ip = ipstr.split(".")
        ans = [ipstr+"/32"]
        range -= 1
        j = 1
        bit_status = 0
        while ip and range>0:
        	cur = int(ip.pop())
        	if cur != 0:
	        	bit_status += int(math.log(cur,2))+1
	        else:
	        	bit_status += 0
	        if cur != 255:
	        	i=32 - bit_status
	        	while range > 0:
	        		range -= int(math.pow(2, bit_status))
	        		ans.append(ipstr+"/"+str(i))
	        		i-=1
        return ans

s=Solution()
ip = "255.86.0.255"
n = 100
print(s.ipToCIDR(ip, n))
