class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, res = [], ""
        for s in strs:
            sizes.append(len(s))
        
        for sz in sizes:
            res += str(sz)
            res += ','
        res += '#'
        print(sizes,res)
        for s in strs:
            res += s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        res=[]

        first_h=s.index('#')
        count=s[:first_h][:-1].split(',')
        e_str=s[first_h+1:]
        print(e_str,count)
        ind=0
        c=0
        for item in count:
            req_cnt=int(item)
            print(req_cnt,e_str)
            word=''
            while req_cnt:
                word+=e_str[0]
                e_str=e_str[1:]
                req_cnt-=1
            res.append(word)
        print(res)
        return res