class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = list(map(lambda x, y: x - y, gas, cost))
        if -sum(filter(lambda x: x < 0, diff)) > sum(filter(lambda x: x > 0, diff)):
            return -1
        n = len(gas)
        cum_tank_diff = 0
        start_index = 0
        for i in range(n):
            cum_tank_diff += gas[i] - cost[i]
            if cum_tank_diff <= 0:
                start_index = i + 1
                cum_tank_diff = 0
        if start_index is None:
            return -1
        start_index = start_index % n
        return start_index