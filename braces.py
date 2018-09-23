def check_if_valid(values):
	braces_stack = []
	pairs = {']':'[', '}':'{', ')':'('}
	left_braces = {'[', '{', '('}
	for cur_brace in values:
		if cur_brace in left_braces:
			braces_stack.append(cur_brace)
		else:
			if not braces_stack:
				return False
			cur_brace_pair = pairs[cur_brace]
			if braces_stack[-1] == cur_brace_pair:
				braces_stack.pop()
			else:
				return False
	if braces_stack:
		return False
	else:
		return True

def braces(values):
	ans = []
	for br_str in values:
		if check_if_valid(br_str):
			ans.append("YES")
		else:
			ans.append("NO")
	return ans

print(braces(["{}", "()", "[]", "{{"]))


