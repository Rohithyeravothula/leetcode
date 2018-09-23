
from collections import Counter

a=[1,2,3,2,1,2,3,1]



distincts = set(a)
l = len(a)
start = 0
end = 0
seen = set(distincts)
counter = Counter()
ans = float("inf")
while end < l:
	while end<l and seen:
		if a[end] in seen:
			seen.remove(a[end])
		counter[a[end]] += 1
		end += 1
	while start<l and counter[a[start]]>1:
		a[start]-=1
		start+=1
	print(start, end)
	if not seen:
		ans = min(ans, end-start+1)
	if start>=l:
		break
	a[start]-=1
	start+=1
	seen = set(distincts)

print(ans)


