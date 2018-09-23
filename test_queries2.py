from collections import defaultdict, Counter

def textQueries(sentences, queries):
	mapping = defaultdict(dict)
	for index, sent in enumerate(sentences):
		sent_counter = Counter(sent.split(" "))
		for word, count in sent_counter.items():
			mapping[word]


	for query in queries:







# inp = ["jim likes mary", "kate likes tom", "tom does not like jim"]
# que = ["jim tom", "likes"]
inp = ["a a"]
que = ["a"]
textQueries(inp, que)
# print(get_sent_subsets(inp[0]))a