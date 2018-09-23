from collections import defaultdict, Counter
from pprint import pprint

def get_all_subsets(words):
	if not words:
		return [[]]
	else:
		subsets = []
		cur_sets = get_all_subsets(words[1:])
		for s in cur_sets:
			subsets.append([words[0]] + s)
			subsets.append(s)
		return subsets

def get_sent_subsets(sent):
	subsets = get_all_subsets(sent.split(" "))
	for s in subsets:
		s.sort()
	return subsets



def textQueries(sentences, queries):
	mapping = defaultdict(set)
	for sent in sentences:
		sent_split = sent.split(" ")
		l = len(sent_split)
		for s in get_sent_subsets(sent):
			key = s
			mapping["-".join(key)].add(sent)
	sent_set_mapping = {sent: (Counter(sent.split(" ")), index) for index, sent in enumerate(sentences)}
	# pprint(mapping)

	for query in queries:
		query_key = list(query.split(" "))
		query_map = Counter(query_key)
		query_key.sort()
		query_sent = mapping["-".join(query_key)]
		# print(query, query_sent)
		response = []
		for sent in query_sent:
			sent_mapping, sent_index = sent_set_mapping[sent]
			common_keys = sent_mapping.keys() & query_map.keys()
			minK = min([sent_mapping[k] for k in common_keys])
			if minK > 0:
				response.extend([str(sent_index)]*minK)
		if response:
			print(" ".join(response))
		else:
			print("-1")





# inp = ["jim likes mary", "kate likes tom", "tom does not like jim"]
# que = ["jim tom", "likes"]
inp = ["a a"]
que = ["a"]
textQueries(inp, que)
# print(get_sent_subsets(inp[0]))