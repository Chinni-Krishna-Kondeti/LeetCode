class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        data = list()
        while i < len(prices) - 1:
            data.append(prices[i + 1] - prices[i])
            i += 1
        s = 0
        for i in data:
            if i > 0:
                s = s + i
        return s