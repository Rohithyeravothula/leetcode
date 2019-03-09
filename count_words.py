def count_words(a):
	l = len(a)
	i = 0
	c = 0
	white_spacechar = {"\n", " ", "\t"}
	while i<l and a[i] in white_spacechar:
		i+=1
	j=l-1
	while j>=0 and a[j] in white_spacechar:
		j-=1
	while i<j:
		if a[i] in white_spacechar:
			c+=1
			while i<j and a[i] in white_spacechar:
				i+=1
		else:
			i+=1
	c+=1
	return c

print(count_words("wow hello"))