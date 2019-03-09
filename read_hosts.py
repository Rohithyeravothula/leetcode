from collections import defaultdict
filename = input()

hosts = defaultdict(int)
with open(filename, 'r') as fp:
	for line in fp.readLines():
		hostname, *_ = line.split(" ")
		hosts[hostname] += 1

with open("records_{}".format(filename), 'w') as fp:
	for key, val in hosts:
		fp.write("{} {}".format(key, val))

