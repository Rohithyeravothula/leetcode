class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        def mask_email(email):
            firstname, info = email.split("@")
            mask = firstname[0].lower() + "*"*5 + firstname[-1].lower()
            mask += "@{}".format(info.lower())
            return mask


        def mask_number(number):
            numlist = [n for n in list(number) if n.isdigit()]
            # print(numlist[-10:])
            num = numlist[-10:]
            mask = ""
            if len(numlist) > 10:
                cc = numlist[:len(numlist) - 10]
                mask = "+" + "*"*len(cc) + "-"
            mask += "***-***-" + "".join(num[-4:])
            return mask

        if "@" in S:
            return mask_email(S)
        return mask_number(S)

s=Solution()
print(s.maskPII("(123)-(456)-(7890)"))



