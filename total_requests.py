from collections import Counter
filename = input()
with open(filename, 'r') as fp:
	data = Counter([line.split()[0] for line in fp.read().split("\n")])

with open("records_"+filename, 'w') as fp:
	rep = ["{} {}".format(key, val) for key, val in data]
	fp.write("\n".join(rep))

