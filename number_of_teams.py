from collections import Counter

def differentTeams(s):
	keys = ['p', 'c', 'm', 'b', 'z']
	counter = Counter(s)
	return min([counter[k] for k in keys])

print(differentTeams("pcmpcmbbzz"))