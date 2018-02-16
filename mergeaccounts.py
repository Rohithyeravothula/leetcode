class UnionFind:
	def __init__(self, l):
		self.ary = [-1]*l

	def find(self, v):
		if self.ary[v] == -1:
			return v
		r = self.find(self.ary[v])
		self.ary[v] = r
		return r

	def add(self, s, e):
		if s!=e:
			sp = self.find(s)
			ep = self.find(e)
			self.ary[sp] = ep


class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        emails = {}
        index = 0
        for account in accounts:
        	for e in account[1:]:
        		if e not in emails:
        			emails[e] = index 
        			index += 1
        l = len(emails)
        ans = []
        mapper = {}
        index = 0
        uf = UnionFind(l)
        for account in accounts:
        	root = float("inf")
        	e1 = account[1]
        	for e in account[2:]:
        		e1i = emails[e1]
        		e2i = emails[e]
        		uf.add(max(e1i, e2i), min(e1i, e2i))

        for account in accounts:
        	""

        		
