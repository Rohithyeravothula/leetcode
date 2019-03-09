# class AnimalSingleTon:
#     animal = None
#     class Animal:
#         count = 0
#         def __init__(self):
#             self.name = "good"
#             AnimalSingleTon.Animal.count += 1

#     def __init__(self):
#         if not AnimalSingleTon.animal:
#             AnimalSingleTon.animal = AnimalSingleTon.Animal()


# a = AnimalSingleTon()
# print(a.animal.name, AnimalSingleTon.Animal.count)
# b = AnimalSingleTon()
# print(a.animal.name, AnimalSingleTon.Animal.count)


class LongInt(int):
    def __init__(self, val):
        self.val = val

class funny_string(str):
    def __init__(self, val):
        self.val = val

    def __get__(self, i):
        return self.val[0]

f = funny_string("hello")
print(f[0], f.__get__(1), f[2])