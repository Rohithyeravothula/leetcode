def print_info(f):
	def f_arge(*args, **kwargs):
		print("called", f.__name__)
		print("args", args, kwargs)
		return f(args, kwargs)
	return f_arge

@print_info
def say_hello():
	name = "world"
	print("hello {}".format(name))


class Test(object):
	name = 32
	def __init__(self, val):
		self.val = val


t1 = Test(1)
# say_hello()
# Test.name = "wow"
t1.name = "now wow"

t2 = Test(2)

print(Test.name)
print(t1.name)
print(t2.name)