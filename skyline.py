# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


    # def get_min_index(a):
    # 	mini = 0
    # 	mine = a[0]
    # 	l = len(a)
    # 	for i in range(0, l):
    # 		if mine >= a[i]:
    # 			mine = a[i]
    # 			mini = i 
    # 	return mini

    # def get_cost(current):
    # 	print(current)
    # 	if len(current) == 0:
    # 		return 0
    # 	if len(current) == 1:
    # 		return current[0]
    # 	mini = get_min_index(current)
    # 	return get_cost(current[:mini]) + get_cost(current[mini+1:])-current[mini]
    # return get_cost(inp)

def solution(inp):
    # write your code in Python 3.6
    l = len(inp)
    cost = 0
    while True:
    	cur_min = min(inp)
    	
    	for i in range(0,l):
    		if inp[i] == cur_min:
    			inp[i] = float("inf")
    		else:
	    		inp[i] -= cur_min




test = [1,2,3,1,2]
print(solution(test))
