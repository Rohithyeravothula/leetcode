from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        counter = defaultdict(int)
        for info in cpdomains:
        	count, domain = info.split(" ")
        	domain_info = domain.split(".")
        	l = len(domain_info)
        	count = int(count)
        	for i in range(0, l):
        		cur_domain = ".".join(domain_info[i:])
        		counter[cur_domain] += count
        result = []
        for item in counter.items():
        	result.append("{} {}".format(item[1], item[0]))
        return result

# inp = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
inp = []
s=Solution()
print(s.subdomainVisits(inp))