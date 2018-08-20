def decode(encoded):
	encoded = encoded[::-1]
	start = 0
	end = 1
	l = len(encoded)
	response = []
	while start < l and end <= l:
		current = int(encoded[start:end])
		if (current >= 65 and current <= 90) or (current >= 97 and current <= 122) or current == 32:
			response.append(chr(current))
			start = end
			end = start + 1
		else:
			end += 1
	return "".join(response)

print(decode(""))
