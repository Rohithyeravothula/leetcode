i=0
next_pos = None
while i<9 and not next_pos:
	j=0
	while j<9 and not next_pos:
		if i*j == 25:
			next_pos = (i, j)
		j+=1
	i+=1

print(next_pos)

