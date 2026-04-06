class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        mp=defaultdict(list)
        for str1 in strings:
            offset=ord(str1[0])-ord('a')
            temp1=''
            for c in str1:
                temp1+=chr((ord(c)-ord('a')-offset)%26+ord('a'))
            #print(temp1)
            mp[temp1].append(str1)

        return list(mp.values())