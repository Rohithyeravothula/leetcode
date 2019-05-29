import re

# re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)


excluded = {"www", "ww2", "web"}
def get_url(text): 
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text) 
    return urls

def get_domain(url):
    info = url.split("://")[1] # ignoring the http or https
    domain = []
    infosplit = [word for word in info.split(".") if word]
    if infosplit and infosplit[0] in excluded:
        del infosplit[0] 
    if len(infosplit) < 2:
        return ""
    infosplit[-1] = re.sub('[^0-9a-zA-Z]+', '', infosplit[-1])
    return ".".join(infosplit)


def getPotentialDomains(lines):
    domain_names = set()
    for line in lines:
        for url in get_url(line):
            domain_names.add(get_domain(url))
    if "" in domain_names:
        domain_names.remove("")
    domain_names = list(domain_names)
    domain_names.sort()
    return ";".join(domain_names)


data = ["https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles"]
data = ["b https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles", "asdkh sfieh (http://www.askford.com/consie_fas/train?view=uk). and what not ", "http://lol.com__", "http://.c"]

with open("html_input.txt", 'r') as fp:
    data = fp.readlines()
# print(len(data))
ans = getPotentialDomains(data)
print(len(ans.split(";")))



# expected = """b.scorecardresearch.com;books.rediff.com;careers.rediff.com;clients.rediff.com;datastore.rediff.com;datastore01.rediff.com;datastore04.rediff.com;datastore05.rediff.com;dealhojaye.rediff.com;hosting.rediff.com;ia.rediff.com;im.rediff.com;imshopping.rediff.com;imworld.rediff.com;investor.rediff.com;ishare.rediff.com;loc.rediff.com;login.rediff.com;mail.rediff.com;metric.ind.rediff.com;money.rediff.com;mypage.rediff.com;n01.rcdn.in;news.rediff.com;pages.rediff.com;realtime.rediff.com;rediff.com;register.rediff.com;search.rediff.com;shopping.rediff.com;simg.rcdn.in;simg03.rcdn.in;track.rediff.com;w3.org;zarabol.rediff.com"""





"""

    for name in infosplit:
        if name == "com":
            domain.append(name)
            break
        domain.append(name)
    return ".".join(domain)

"""