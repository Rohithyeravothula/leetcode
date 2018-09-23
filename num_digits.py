class Solution(object):
    def atMostNGivenDigitSet(self, d, n):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        def count(num_of_digits, fd, mapper):
        	fdc = len([r for r in d if fd > r])
        	ans = fdc*mapper[num_of_digits-1]
        	
        	for i in range(1, num_of_digits):
        		ans += mapper[i]
        	# print(ans, fdc, num_of_digits)
        	return ans

        d = [int(r) for r in d]
        dl = len(d)
        c = dl
        mapper = {0:1}
        for i in range(1, 10):
        	mapper[i] = c
        	c*=dl
        n = str(n)
        nl = len(n)
        if nl == 1:
        	return len([r for r in d if int(n) <= r])
        ans = 0
        for i,v in enumerate(n):
        	if v  != "0" and int(v) in d:
	        	ans += count(nl-i, int(v), mapper)
	        elif int(v) not in d:
	        	cur_count = len([r for r in d if int(v) > r])
	        	ans += cur_count*mapper[nl-i-1]
	        	break

        # print(ans)
        return ans

D = ["3", "4", "8"]
N = 44

# D = ["1","4","9"]
# N = 1000000000

# D = ["7"]
# N = 8

print(Solution().atMostNGivenDigitSet(D, N))
        