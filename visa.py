
import string
def decode(encoded):
	valid = {ord(char) for char in string.ascii_letters}
	valid.add(32)
	encoded = encoded[::-1]

	cur = 0
	start = 0
	l = len(encoded)
	found = []


	while cur < l:
		number = int(encoded[start:cur+1])
		if number in valid:
			found.append(number)
			cur += 1
			start = cur
		else:
			cur += 1

	if start < cur:
		found.append(int(encoded[start:cur]))
	print(found)
	return "".join([chr(number) for number in found])

# enc = "1219950180111108236115111016623101401611235115012312161151110101111127"
enc = "07"
print(decode(enc))