class Solution(object):
    def brokenCalc(self, x, y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        if x >= y:
            return x-y
        count = 0
        while True:
            if y==x:
                return count
            elif y+1 == x:
                return count+1
            elif y%2==0 and y>x:
                y = y>>1
            else:
                y+=1
            count += 1
while True:
    a,b = map(int, input().split())
    print(Solution().brokenCalc(a,b))
        