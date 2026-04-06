class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp=defaultdict(list)

        for item in strs:
            temp="".join(sorted(item))
            mp[temp].append(item)
        return list(mp.values())