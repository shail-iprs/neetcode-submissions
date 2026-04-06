class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp=defaultdict(list)

        for item in strs:
            temp=tuple(sorted(item))
            mp[temp].append(item)
        return [mp[item] for item in mp.keys()]
