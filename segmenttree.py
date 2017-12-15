def seg_tree(seg, i, s, e, a, n):
	if s == e:
		seg[i] = a[s]
	elif s<e:
		seg_tree(seg, 2*i+1, s, int((s+e)/2), a, n)
		seg_tree(seg, 2*i+2, 1+int((s+e)/2), e, a, n)
		if 2*i+1 < n and 2*i+2 < n:
			seg[i] = seg[2*i+1] + seg[2*i+2]
		elif 2*i+1 < n:
			seg[i] = seg[2*i+1]

def get_sum_recr(seg, i, rs, re, s, e, n):
	if s>e or i>=n:
		return 0
	elif rs==re:
		if rs>=s and rs<=e:
			return seg[i]
		return 0
	elif s>=rs and re<=e:
		return seg[i]
	else:
		return get_sum_recr(seg, 2*i+1, rs, int((rs+re)/2), s, e, n) + get_sum_recr(seg, 2*i+2, 1+int((rs+re)/2), re, s ,e, n)

def update(seg, i, s, e, j, diff, n):	
	if i<n and s<=j and e>=j:
		seg[i] = seg[i] + diff
		update(seg, 2*i+1, s, int((s+e)/2), j, diff, n)
		update(seg, 2*i+2, 1+int((s+e)/2), e, j, diff, n)

def get_sum(seg, s, e, l):
	return get_sum_recr(seg, 0, 0, l-1, s, e, len(seg))


a=[1,2,3,4,5]
l = len(a)
n = 2*l-1
seg = [0]*n
seg_tree(seg, 0, 0, l-1, a, n)
print(get_sum(seg, 0, 3, l))
diff = 8-a[2]
update(seg, 0, 0, l-1, 2, diff)
print(get_sum(seg, 0, 3, l))