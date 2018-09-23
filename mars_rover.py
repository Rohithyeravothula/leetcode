def roverMove(n, cmds):
	i=0
	j=0
	for cmd in cmds:
		if cmd == "UP":
			i = max(0, i-1)
		elif cmd == "DOWN":
			i = min(n-1, i+1)
		elif cmd == "LEFT":
			j = max(0, j-1)
		elif cmd == "RIGHT":
			j = min(n-1, j+1)
	return (i*n)+j

print(roverMove(4, ["RIGHT", "UP", "DOWN", "LEFT", "LEFT", "DOWN", "DOWN"]))
