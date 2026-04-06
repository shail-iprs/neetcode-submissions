class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res=set()
        for addr in emails:
            temp=addr.split('@')
            first=temp[0]
            second=temp[1]

            first=first.split('+')[0].replace('.','')
            second=second.replace('+','')
            print(addr,first+'@'+second)
            res.add(first+'@'+second)
        return len(res)