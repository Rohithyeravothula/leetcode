def decode(s):
	s = s[::-1]
	l = len(s)
	i = 0
	j = 1
	caps_range = range(ord('A'), ord('Z')+1)
	small_range = range(ord('a'), ord('z')+1)
	ans = []
	while j<=l:
		cur = int(s[i:j])
		if cur in caps_range or cur in small_range or cur == 32:
			ans.append(chr(cur))
			i = j
			j = i+1
		else:
			j+=1
	return "".join(ans)


s="23511011501782351112179911801562340161171141148"
print(decode(s))
			


