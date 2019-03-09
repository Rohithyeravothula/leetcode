def deleteProducts(ids, m):
	counter = {}
	for val in ids:
		if val in counter:
			counter[val] += 1
		else:
			counter[val] = 1
	items = [(val, key) for key, val in counter.items()]
	items.sort()
	total_items = len(items)
	item_index = 0
	while item_index<total_items:
		m -= items[item_index][0]
		if m<0:
			break
		item_index+=1
	return total_items - item_index