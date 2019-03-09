class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        seen = set()
        for email in emails:
            first, domain = email.split("@")
            first, *_ = first.split("+")
            first = first.replace(".", "")
            seen.add("{}@{}".format(first, domain))
        return len(seen)

inp = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
inp = ["a+.test@email.com", "a+@email.com"]
print(Solution().numUniqueEmails(inp))

