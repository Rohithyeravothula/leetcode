def insert_in_sorted_stack(a, n):
	if not a:
		a.append(n)
	else:
		cur = a.pop()
		if cur > n:
			a.append(cur)
			a.append(n)
		else:
			insert_in_sorted_stack(a, n)
			a.append(cur)


def sort_stack(a):
	if not a:
		return a
	cur = a.pop()
	sort_stack(a)
	insert_in_sorted_stack(a, cur)



def pop_num(a, n):
	if not a:
		return
	cur = a.pop()
	if cur == n:
		return 
	else:
		pop_num(a, n)
		a.append(cur)




# cst = [80, 44, 20, 5, 2, 1]
cst = [1,1,1,1,2]
# cst = [5]
# sort_stack(cst)
# insert_in_sorted_stack(cst, 4)
# pop_num(cst, 20)
bubble_sort(cst)
print(cst)