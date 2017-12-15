class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        d = {}
        for pair in tickets:
            if pair[0] in d:
                d[pair[0]].append(pair[1])
            else:
                d[pair[0]] = [pair[1]]

        for pair in d:
            d[pair].sort()

        itinerary = ["JFK"]
        cur = "JFK"
        print(d)
        while cur in d and d[cur] != []:
            print(d)
            nxt = d[cur]
            d[cur] = nxt[1:]
            itinerary.append(nxt[0])
            cur = nxt[0]
        return itinerary

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
s = Solution()
print(s.findItinerary(tickets))