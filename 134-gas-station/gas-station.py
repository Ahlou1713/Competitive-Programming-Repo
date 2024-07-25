class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(cost)

        if sum(cost) > sum(gas):
            return -1
        
        total = 0
        output = 0

        for i in range(n):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                output = i + 1


        return output