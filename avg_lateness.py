from collections import defaultdict
def latestStudent(a):
	if not a:
		return ""
	dates = defaultdict(list)
	for (date, name, start, end) in a:
		dates[date].append([name, max(int(end)-int(start), 0)])
	lateness = defaultdict(int)
	for d, info in dates.items():
		avg_lateness = sum([t for _, t in info])/len(info)
		for name, t in info:
			cur_late = max(0, t - avg_lateness)
			lateness[name] += cur_late
	max_late, _ = max([(val, name) for name, val in lateness.items()])
	names = [name for name, val in lateness.items() if val == max_late]
	
	return min(names)

inp = [
["09-01","Berlene","540","570"],
["09-01","Bobby","540","570"],
["09-01","Caroline","540","530"],
["09-02","Arlene","540","580"],
["09-02","Bobby","540","580"],
["09-02","Caroline","540","595"]]
print(latestStudent(inp))
