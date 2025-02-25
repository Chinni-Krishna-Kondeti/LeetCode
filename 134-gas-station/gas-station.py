class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        n = len(gas)
        cum_tank_diff = 0
        start_index = 0
        for i in range(n):
            cum_tank_diff += gas[i] - cost[i]
            if cum_tank_diff < 0:
                start_index = i + 1
                cum_tank_diff = 0
        return start_index