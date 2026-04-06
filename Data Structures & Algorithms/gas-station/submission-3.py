class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_cost=sum(cost)
        total_gas=sum(gas)
        if total_cost>total_gas:
            return -1
        start=0
        curr=0
        for ind in range(len(gas)):
            curr+=gas[ind]-cost[ind]
            if curr<0:
                start=ind+1
                curr=0
        return start
