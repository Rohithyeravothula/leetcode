
x=123
y=3
count = 0
while x or y:
    print(count, x, y)
    count += x%2 ^ y%2
    x=x>>1
    y=y>>1
print(count)