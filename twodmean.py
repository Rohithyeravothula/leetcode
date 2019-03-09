def get_length(val):
    c=0
    for v in val:
        if v!=0:
            c+=1
    return c

def mean(two_d_array):
    m = []
    for val in two_d_array:
        s = sum(val)
        l = get_length(val)
        if s%l == 0:
            m.append(s//l)
        else:
            cm = round(float(s)/l, 1)
            m.append(cm)
    print(m)
    return m

inp = [[-1,3,1], [0,1,1],[4,3,1]]
mean(inp)



from collections import Counter
def max_logs(domain, logs):
    counter = Counter()
    for log in logs:
        info, date = log.split(".com")
        _, name = info.split("@")
        if name == domain:
            counter[date] += 1
    max_date = None
    max_val = 0
    for date, val in counter.items():
        if val > max_val:
            max_val = val
            max_date = date
    # print(max_date) 
    return max_date