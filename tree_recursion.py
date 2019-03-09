from collections import defaultdict

def build(tree, cur):
	if cur is None:
		return ""
	elif cur not in tree:
		return "{}".format(cur)

	left = build(tree, tree[cur][0])
	right = build(tree, tree[cur][1])
	return "({}){}({})".format(left, cur, right)
	

def sExpression(nodes):
	tree = {}
	for p,c in nodes:
		if p not in tree:
			tree[p] = [None, None]
		if tree[p][0] is None:
			tree[p][0] = c
		elif tree[p][1] is None:
			tree[p][1] = c 
		elif c == tree[p][0] or c == tree[p][1]:
			return "E2"
		else:
			return "E1"
	rep = build(tree, 'A')
	print(rep)


inp = [('A', 'B'), ('B', 'C'),('B', 'D')]
sExpression(inp)


"""
sivagrubhuborder@gmail.com

Fskfu#234ks

3478396457


"""