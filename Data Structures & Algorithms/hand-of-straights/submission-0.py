class Solution:
    def isNStraightHand(self, hand: List[int], gs: int) -> bool:
        n=len(hand)
        if n%gs!=0:
            return False
        
        mp=Counter(hand)
        #print(mp)
        hand.sort()
        #print(hand)
        count=0
        for ind in range(n):
            val=hand[ind]
            if mp[val]>0:
                #print(list(range(val,val+4)))
                for idx in range(val,val+gs):
                    print('idx:',idx)
                    if mp[idx]==0:
                        return False
                    mp[idx]-=1
        return True