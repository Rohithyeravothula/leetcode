def heapify(a):
    length = len(a)
    i = length//2
    while i>=0:
        p = a[i]
        l = a[2*i+1] if (2*i+1) < length else -float('inf')
        r = a[2*i+2] if (2*i+2) < length else -float('inf')
        if p<l or p<r:
            if l<r:
                a[i], a[2*i+2] = a[2*i+2], a[i]
            else:
                a[i], a[2*i+1] = a[2*i+1], a[i]
        i-=1

def extractmin(a):
    length = len(a)
    # replace first elemenent with last one
    val = a[0]
    a[0] = a[-1]
    i=0
    while i<length:
        p = a[i]
        l = a[2*i+1] if (2*i+1) < length else -float('inf')
        r = a[2*i+2] if (2*i+2) < length else - float('inf')
        if p<l or p<r:
            if l<r:
                a[i], a[2*i+2] = a[2*i+2], a[i]
                i = 2*i+2
            else:
                a[i], a[2*i+1] = a[2*i+1], a[i]
                i = 2*i+1
        else:
            break
    a.pop()
    return val

# def heapsort(a):


a = [5,4,3,2,1]
heapify(a)
print(a)
while a:
    print(extractmin(a))
