def fetchItemsToDisplay(items, sortParameter, sortOrder, itemPerPage, pageNumber):
	items.sort(key=lambda x: int(x[sortParameter]) if sortParameter > 0 else x[sortParameter], reverse=sortOrder==1)
	return [n for n,_,_ in items[pageNumber*itemPerPage: (1+pageNumber)*itemPerPage]]

print(fetchItemsToDisplay([["p1", "1", "2"], ["p2", "2", "1"]], 0, 0, 1,0))
