from collections import Counter

def max_logs2(domain, logs):
    counter = Counter()
    for log in logs:
        info, date = log.split(".com")
        user, name = info.split("@")
        name += ".com"
        if name == domain:
            counter[int(date)] += 1
    counter = [(val, date) for date, val in counter.items()]
    counter.sort()
    max_val = 0
    max_data = None
    print(counter)
    for val, key in counter:
        if val > max_val:
            max_val = val 
            max_data = key
    print(max_data)
    return max_data

def test(log):
    if len(log.split("@")) != 2:
        print(log.split("@"))
    else:
        return None
    

def max_logs(domain, logs):
    for log in logs:
        test(log)

max_logs("", ["user1@@org.com12345678"])

def max_logs(domain, logs):
    counter = Counter()
    for log in logs:
        counter[log[-8:]] += 1
    counter = [(val, key) for key, val in counter.items()]
    counter.sort()
    print(counter)
    print(counter[-1][1])
    return counter[-1][1]



# dom = "organisation1.com"
# inp = ['user1@organisation1.com20180912', 'user3@organisation1.com20180912', 'user4@organisation1.com20180912', 'user2@organisation2.com20180912', 'user2@organisation1.com20180911', 'user2@organisation1.com20180912']

# dom = 'organisation2.com'
# inp = ['user1@organisation1.com20180910', 'user3@organisation1.com20180912', 'user4@organisation1.com20180912', 'user2@organisation2.com20180912', 'user2@organisation1.com20180911', 'user4@organisation2.com20180912', 'user5@organisation2.com20180910', 'user6@organisation2.com20180910', 'user2@organisation1.com20180910']

# max_logs(dom, inp)
# max_logs2("what", ["user@wh.comat.com12345678"])

"""
        *info, date = log.split(".com")
        info = ".com".join(info)
        _, *name= info.split("@")
        name = "@".join(name)
"""