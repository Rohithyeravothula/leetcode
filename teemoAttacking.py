class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        i=1
        l=len(timeSeries)
        start = timeSeries[0]
        end = timeSeries[0]+duration
        total = 0
        while i<l:
            if end < timeSeries[i]:
                total += end - start
                start = timeSeries[i]
                end = timeSeries[i] + duration
            else:
                end = max(end, timeSeries[i]+duration)
            i+=1
        total = total + end - start
        return total


a=[1,2,3,4,5,6]
s=Solution()
print(s.findPoisonedDuration(a,2))