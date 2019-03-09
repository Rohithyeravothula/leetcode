from collections import deque
class RecentCounter:

    def __init__(self):
        self.cur = deque([])


    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.cur.append(t)
        while self.cur:
        	if self.cur[0] < t-3000:
        		self.cur.popleft()
        	else:
        		break
        return len(self.cur)



        


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))
print(obj.ping(9002))