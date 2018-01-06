def small_compare(number, l):
	left = number[:l]
	right = number[::-1][:l]
	if int(left) < int(right):
		return False
	return True

# print(small_compare("14", 1))

def compare(left, right):
	left = str(left)
	right = str(right)
	left_length = len(left)
	right_length = len(right)
	ans = True # says left is bigger to right
	i=0 # left index
	j=0 # right index
	while i<left_length and j<right_length:
		if int(left[i]) < int(right[j]):
			ans = False
			break
		elif int(left[i]) == int(right[j]):
			i+=1
			j+=1
		else:
			break
	# when right is less than left
	if i==left_length and j!=right_length and left == right[0:i]:
		ans = small_compare(right, i)
	elif j==right_length and i!=left_length and left[0:j] == right:
		ans = not small_compare(left, j)

	if ans:
		print("{} < {}".format(right, left))
		return 1
	else:
		print("{} < {}".format(left, right))
		return -1


def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = sorted(nums, key=cmp_to_key(compare), reverse=True)
        # print(nums)
        return "".join(list(map(lambda x: str(x), nums)))

s=Solution()
# print(s.largestNumber([9,98]))
# print(s.largestNumber([98,9]))
print(s.largestNumber([9810273,8917]))
# a=[4,2,3,1,23,1,987,907,9810273,8917,234,1,23,41,23,4,1,23,41,23,41,23,41,234,12,34,1234,123,41,9]
# print(s.largestNumber(a))
# print(s.largestNumber([56,5]))
# print(s.largestNumber([14, 1]))
        
# compare(14,1)

# compare(132451, 981073245)
# print(compare(1,14))
# compare(1,2)
# compare(2,2)
# compare(11,2)
# compare(1,22)
# compare(9, 98)
# compare(9, 91)
# compare(29, 98)
# compare(99, 98)
# compare(20, 98)
# compare(90, 98)
# compare(199, 98)