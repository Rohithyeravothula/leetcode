class Student():
    def __init__(self, name, sid):
        self.name = name
        self.id = sid

    # def __hash__(self):
    #     return len(self.name) + self.id

    def __repr__(self):
        return "name: {}, id: {}".format(self.name, self.id)


s = Student("hello", 1)
d = {}
d[s] = 1
print(hash(s))
s.name = "wow"
print(s)
print(hash(s))
print(d[s])