# Complete the function below.


def  css_string_to_color(colorString):
    if colorString == "" or colorString[0] != "#":
        raise Exception("error")
    else:
        colorString = list(colorString[1:])
        l = len(colorString)
        if l==3:
        	tmp = []
        	for i in colorString:
        		tmp.append(i)
        		tmp.append(i)
        	colorString = tmp
        ans = 0
        print(colorString)
        l = len(colorString)
        i=1
        mult = 0
        while i<l:
        	cur = colorString[i-1]+colorString[i]
        	num = int(cur, 16)
        	# print(cur, num)
        	num = num << mult
        	ans += num
        	i+=2
        	mult += 8
        return ans

# print(css_string_to_color("#800080"))