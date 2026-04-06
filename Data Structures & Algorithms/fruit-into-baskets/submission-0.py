class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mp={}
        left=0
        res=0
        total=0
        for right in range(len(fruits)):
            mp[fruits[right]]=mp.get(fruits[right],0)+1
            total+=1

            while len(mp)>2:
                mp[fruits[left]]-=1
                total-=1
                if mp[fruits[left]]==0:
                    del mp[fruits[left]]
                left+=1
            
            res=max(res,total)
        return res