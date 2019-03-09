class Solution:
    def minFlipsMonoIncr(self, s):
        """
        :type S: str
        :rtype: int
        """
        l = len(s)
        oc = [0]
        for i in range(l):
        	if s[i] == '1':
        		oc.append(oc[-1]+1)
        	else:
        		oc.append(oc[-1])

        zc = [0]*(l+1)
        for j in range(l-1, -1, -1):
        	if s[j] == '0':
        		zc[j] = zc[j+1]+1
        	else:
        		zc[j] = zc[j+1]

        print(oc)

        m = zc[0]
        for i in range(1, l):
        	print(i, oc[i], zc[i+1])
        	m = min(oc[i]+zc[i+1], m)
        return m



t = "010110"
t = "1110000"
print(Solution().minFlipsMonoIncr(t))

