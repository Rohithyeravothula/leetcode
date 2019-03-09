
def missingWords(s, t):
	s = s.split()
	t = t.split()
	sl = len(s)
	tl = len(t)
	i = 0
	j = 0
	ans = []
	while i<sl and j<tl:
		if s[i] == t[j]:
			i+=1
			j+=1
		else:
			ans.append(s[i])
			i+=1
	while i<sl:
		ans.append(s[i])
		i+=1
	return ans

s = ""
t = ""
print(missingWords(s,t))



"""
internship
bay area
team work
team 
company career 

domain: travelling domain <= narrow


alignment of the team

paypal
re-platform metric ingest layer metric db
machine learning can't have now, next leap
ttd and ttr 

fintech => good market
systems team




don't try out 


compensation 


"""