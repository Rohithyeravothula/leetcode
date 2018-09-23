from collections import Counter
def find_intersection_between_lists(l1, l2):
	l1c = Counter(l1)
	ans = []
	for val in l2:
		if val in l1c and l1c[val] > 0:
			ans.append(val)
			l1c[val] -= 1
	return ans

def textQueries(sentences, queries):
	word_map = {}
	for index, sent in enumerate(sentences):
		for word in sent.split():
			if word in word_map:
				word_map[word].append(index)
			else:
				word_map[word] = [index]
	for query in queries:
		response = None
		for word in query.split():
			if word in word_map:
				cur = word_map[word]
				if response is None:
					response = cur
				else:
					response = find_intersection_between_lists(response, cur)
			else:
				response = []
				break
		if not response:
			print("-1")
		else:
			print(" ".join([str(i) for i in response]))

# sentences = ["how it was done","are done you how it it", "it goes to","goes done are it"]
# queries = ["done it it"]

sentences = ["it go will away", "go do art" ,"what to will east"]
queries= ["it will", "go east will", "will"]
textQueries(sentences, queries)


