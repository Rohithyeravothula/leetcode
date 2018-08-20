from collections import Counter
def textQueries(sentences, queries):
	sent_repr = {sent: Counter(sent.split()) for sent in sentences}
	quer_repr = {query: set(query.split()) for query in queries}
	for qi, query in enumerate(queries):
		response = []
		for si, sent in enumerate(sentences):
			if quer_repr[query].intersection(sent_repr[sent].keys()) == quer_repr[query]:
				response.append(str(si))
		if not response:
			print("-1")
		else:
			print(" ".join(response))



sents = ["bob and alice like to text", "bob does not like ski", "alice likes ski"]
ques = ["bob alice", "alice", "like", "asf"]
print(textQueries(sents, ques))
