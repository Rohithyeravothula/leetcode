import math
import os
import random
import re
import sys



from collections import defaultdict
def socialGraphs(counts):
	total = len(counts)
	groups = defaultdict(list)
	for index, size in enumerate(counts):
		groups[size].append(str(index))

	print(groups)

	for index, size in enumerate(counts):
		if groups[size] and groups[size][0] == str(index):
			curgroup = groups[size][:size]
			updated = groups[size][size:]
			print(" ".join(curgroup))
			groups[size] = updated

counts = [1,1,1,1]
counts = [3,3,3,3,3,1,3]
counts = [2,2,2,2]
counts = [2,1,1,2,1]
socialGraphs(counts)



