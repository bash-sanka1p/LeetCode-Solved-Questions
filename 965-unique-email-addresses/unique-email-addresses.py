class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s=set()
        for email in emails:
            splitted = email.split('@')
            localname = splitted[0]
            localname=list(localname.split("+")[0])
            while "." in localname:
                localname.remove(".")
            new_email = "".join(localname)+"@"+splitted[1]
            s.add(new_email)
            print(new_email)
        return len(s)