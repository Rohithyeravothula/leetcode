def getWindowedComplement(n, lo, hi):
    if lo > hi or lo not in range(0, 16) or hi not in range(0, 16):
        return 0
    m = ((1<<(1+hi))-1) ^ ((1<<l0)-1)
    return n^m


def CountOverlaps(ranges):
    d = []
    l = len(ranges)
    for i in range(1, l, 2):
        d.append((ranges[i-1], ranges[i]))
    # print(d)
    si = sorted(d, key=lambda tup: tup[0])
    merged = []
    for tup in si:
        if not merged:
            merged.append(tup)
        else:
            b = merged.pop()
            if b[1] >= tup[0]:
                new_tup = tuple([b[0], tup[1]])
                merged.append(new_tup)
            else:
                merged.append(b)
                merged.append(tup)
    return l/2 - len(merged)



inp = [1, 10, 3, 5, 4, 9]
s = CountOverlaps(inp)
print(s)


"""


A process is an executing instance of a program,
which has its unique process identifier, environment variables, 
separate memory(heap and stack) space, file descriptors, system context
signal handling context, security context and a main thread of execution.
They are controlled by operating system and are considered to be independent.

A thread is a single unit of execution on CPU. Every process has one
main thread. Threads are light weight, they share its parent process 
virtual address space and system resources. Each thread maintains its own 
exception handlers, thread local storage, unique thread identifier, file pointers
and stack.



On a single processor machine and a desktop application, you use multi threads so you don't freeze the app but for nothing else really.
On a single processor server and a web based app, no need for multi threading because the web server handles most of it.
On a multi-processor machine and desktop app, you are suggested to use multi threads and parallel programming. 
Make as many threads as there are processors.
On a multi-processor server and a web based app, no need again for multi threads because the web server handles it.
"""