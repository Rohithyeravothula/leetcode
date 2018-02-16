n,m = map(int, input().split(" "))
names = {}
for i in range(0,n):
	server, ip = input().split(" ")
	names[ip] = server


for i in range(0, m):
	full = input()
	server, ip = full.split(" ")
	full += " #"+names[ip[:-1]]
	print(full)
