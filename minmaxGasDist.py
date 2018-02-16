from heapq import heappush, heappop
class Solution:
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        dist = []
        l = len(stations)
        for i in range(1, l):
        	print(stations[i] - stations[i-1])
        	heappush(dist, -1*(stations[i] - stations[i-1]))

        while K>0:
        	print(dist)
        	top = -1*heappop(dist)
        	next_top = -1*dist[0]
        	r = 1+ int(top//next_top)
        	if r <= K:
        		K-=(r-1)
        	else:
        		r = K+1
        		K = 0
        	new_dist = top/r
        	for i in range(0, r):
        		heappush(dist, -1*new_dist)
        return -1*heappop(dist)

ss = [10,19,25,27,56,63,70,87,96,97]
kk = 3
s=Solution()
print(s.minmaxGasDist(ss, kk))

        