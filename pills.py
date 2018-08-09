maxp = 0
maxr = 0
maxb = 0
for x in range(0, 101):
    for y in range(0, 101):
        if not x and not y or x==100 and y == 100:
            continue
        curp = 0.5*((x/(x+y)) + ((100-x)/(200-x-y)))
        if curp > maxp:
            maxr = x
            maxb = y
            maxp = curp
print(maxp, maxr, maxb, 100-maxr, 100-maxb)
