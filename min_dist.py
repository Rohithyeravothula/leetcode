class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        dist = []
        i = 0
        l = len(seats)
        while i<l and seats[i] == 0:
            dist.append(float("inf"))
            i+=1

        while i<l:
            if seats[i] == 0:
                dist.append(dist[i-1]+1)
            else:
                dist.append(0)
            i+=1
        # print(dist)

        i = l-1
        while i >= 0 and seats[i] == 0:
            i-=1

        while i>=0:
            if seats[i] == 0:
                dist[i] = min(dist[i], dist[i+1]+1)
            i-=1
        max_dist = 0
        print(dist)
        print(seats)
        for i in range(0, l):
            if seats[i] == 0 and max_dist < dist[i]:
                max_dist = dist[i]
        return max_dist


# sts = [0,0,0,1,1,1,0,0,1,1]
sts = [1,1,1,1,0,1,1,1  ]
s = Solution()
print(s.maxDistToClosest(sts))