from collections import Counter

def get_info(log):
	date = ""
	l = len(log)
	i = l-1
	while i>=0:
		if log[i].isnumeric():
			date = log[i] + date
			i-=1
		else:
			break

	name = ""
	j = 0
	while j<=i and log[j] != "@":
		j+=1
	j+=1
	while j<=i:
		name += log[j]
		j+=1
	return name, date



def max_logs(domain, logs):
	counter = Counter()
	for log in logs:
		name, date = get_info(log)
		print(name, date)
		if domain == name and date.isnumeric():
			counter[date] += 1
	values = [(val, int(key)) for key, val in counter.items()]
	max_val = max([val for val, _ in values])
	values = [(val, key) for val, key in values if val == max_val]
	values.sort(key = lambda x: x[1])
	# print(values)
	ans = str(values[0][1])
	# print(ans)
	return ans

dom = "organisation1.com"
inp = ['user1@organisation1.com20180912', 'user3@organisation1.com20180912', 'user4@organisation1.com20180912', 'user2@organisation2.com20180912', 'user2@organisation1.com20180911', 'user2@organisation1.com20180912']

# dom = 'organisation2.com'
# inp = ['user1@organisation1.com20180910', 'user3@organisation1.com20180912', 'user4@organisation1.com20180912', 'user2@organisation2.com20180912', 'user2@organisation1.com20180911', 'user4@organisation2.com20180912', 'user5@organisation2.com20180910', 'user6@organisation2.com20180910', 'user2@organisation1.com20180910']

max_logs(dom, inp)