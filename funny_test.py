import random
def ch():
    print("*", end="") if random.randint(0, 1)%2==1 else print("-", end="")

while True:
    ch()
