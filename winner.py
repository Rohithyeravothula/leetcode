def winner(andrea, maria, s):
	i = 0
	l = len(andrea)
	if s == "Odd":
		i+=1
	and_score = 0
	mar_score = 0
	while i<l:
		and_score += (andrea[i] - maria[i])
		mar_score += (maria[i] - andrea[i])
		i+=2
	if and_score > mar_score:
		return "Andrea"
	elif and_score < mar_score:
		return "Maria"
	else:
		return "Tie"

print(winner([1,2,3], [1,1,3], "Even"))