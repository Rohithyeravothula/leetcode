def usernamesSystem(u):
	d = {}
	response = []
	for user in u:
		if user in d:
			response.append(user + str(d[user]))
			d[user] += 1
		else:
			response.append(user)
			d[user] = 1
	return response

print(usernamesSystem([]))
