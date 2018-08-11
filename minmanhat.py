from heapq import heappush, heappop

n = int(input())
e = int(input())
events = {}
for i in range(0, e):
	info = input().split(" ")
	prices = list(map(lambda x: int(x), info[3:]))
	prices.sort()
	events[int(info[0])] = [(int(info[1]), int(info[2])), prices]

t = int(input())
for ticket in range(0, t):
	x,y = map(int, input().split(" "))
	min_events_detail = []
	for event in events.keys():
		event_info = events[event]
		ex,ey = event_info[0]
		dist = abs(x-ex) + abs(y-ey)
		if len(event_info[1]) > 0:
			min_events_detail.append[(min_events_detail, (dist, event, event_info))]

	if len(min_events_detail) > 0:
		min_events_detail.sort()
		minprice = min_events_detail[0][0]
		min_events_detail = list(filter(lambda x: x == minprice, min_events_detail))
		min_details = min_events_detail
		min_dist = min_details[0]
		min_price_list = min_details[2][1]
		min_price_id = min_details[1]
		if len(min_price_list) > 0:
			min_price = min_price_list[0]
			del min_price_list[0]
			print(min_price_id, min_price)
		else:
			print(-1, 0)
	else:
		print(-1, 0)



usc 2017 spring india admits
usc fall 2016 
usc room roommates subleasing
association of india
free and for sale