def flatten(lst):
	flatten_elements = []
	for i in lst:
		if isinstance(i, str):
			flatten_elements.append(i)
		else:
			elements = flatten(i)
			for e in elements:
				flatten_elements.append(e)
	return flatten_elements

if __name__ == "__main__":
	test = ["level1", ["level2", [["level3"]]]]
	print(flatten(test))