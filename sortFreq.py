from collections import Counter
def customSort(arr):
    counter = [(val, key) for key, val in Counter(arr).items()]
    counter.sort()
    print(counter)
    for val, key in counter:
        for _ in range(val):
            print(key)

customSort([3,1,2,2,4])